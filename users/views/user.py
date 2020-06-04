from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from users.serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer, PasswordChangeSerializer, LostPasswordChangeSerializer
from django.contrib.auth import get_user_model
import uuid
from users.feeds import UserRepository, create_activate_token
from django.core.mail import send_mail
from django.http import Http404
from users.models import Pattern
from rest_framework.decorators import action
from django.conf import settings
from users.permissions import UserPermissionMixin
from companies.models import Classroom

User = get_user_model()


class UserViewSet(UserPermissionMixin, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, viewsets.GenericViewSet):

    queryset = User.objects.all().order_by('first_name')
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer

        if self.action == 'update':
            return UserUpdateSerializer

        return UserSerializer

    # roles
    @action(methods=['GET'], detail=False)
    def roles(self, request, *args, **kwargs):
        user_id = request.user.id

        user_roles = Pattern.objects.filter(role__user_id=user_id).all()

        companies = []
        role_types = []
        roles = []

        for user_role in user_roles:
            role_add = 1
            r_sub = {}
            content_type = user_role.content_type.model

            if content_type == 'companygroup' or content_type == 'school':
                company_id = user_role.object_id
                company_name = user_role.content_object.name

            elif content_type == 'classroom':

                company_id = user_role.content_object.school.id
                company_name = user_role.content_object.school.name

                r_sub = {
                    'id': user_role.object_id,
                    'name': user_role.content_object.name
                }
            elif content_type == 'classroomlesson':

                company_id = user_role.content_object.classroom.school.id
                company_name = user_role.content_object.classroom.school.name

                r_sub = {
                    'id': user_role.object_id,
                    'name': user_role.content_object.lesson.name
                }
            elif content_type == 'publisher':
                company_id = user_role.object_id
                company_name = user_role.content_object.name
            elif content_type == 'user':
                company_id = 0
                company_name = 'Educate'
            else:
                role_add = 0


            if role_add == 1:
                r_company = {
                    'id': company_id,
                    'name': company_name,
                    'type': content_type
                }


                r_role_types = {
                    'id': user_role.role.group.id,
                    'name': user_role.role.group.name,
                    'page': settings.ROLE_PAGES[user_role.role.group.id]
                }

                r_roles = {
                    'id': user_role.id,
                    'role_user_id': user_role.role_id,
                    'company': r_company,
                    'role': r_role_types,
                    'class': r_sub
                }

                roles.append(r_roles)

                if r_company not in companies:
                    companies.append(r_company)

                if r_role_types not in role_types:
                    role_types.append(r_role_types)

        response = {
            'roles': roles,
            'role_types': role_types
        }

        return Response(response, status=status.HTTP_200_OK)

    # search
    @action(methods=['POST'], detail=False)
    def search(self, request, *args, **kwargs):
        key = request.data.get('key')
        value = request.data.get('value')

        if key == 'email':
            user = User.objects.filter(email=value).first()
        else:
            user = User.objects.filter(identity_number=value).first()

        serializer = self.get_serializer(user)
        return Response(serializer.data)

    # permissions
    @action(methods=['GET'], detail=False)
    def permissions(self, request, *args, **kwargs):
        pass

    # profile
    @action(methods=['GET'], detail=False)
    def profile(self, request, *args, **kwargs):
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        serializer = self.get_serializer(user)

        queryset = Classroom.objects.filter(student=user).all()
        course_ids = queryset.values_list('id', flat=True)

        data = {
            'profile': serializer.data,
            'courses': course_ids
        }
        return Response(data)

    # kullanıcı siler
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # log out
    # çıkış yapıldığında token yenilenir. Tüm platformlarda sistemden çıkış yapılır.
    @action(methods=['GET'], detail=False)
    def logout(self, request, *args, **kwargs):

        ur = UserRepository(user=request.user)
        ur.change_token()

        return Response(status=status.HTTP_200_OK)

    # change password
    # şifre değiştirildiğinde token yenilenir. Diğer tüm platformlarda sistemden çıkış yapılır.
    @action(methods=['POST'], detail=False)
    def change_password(self, request, *args, **kwargs):

        user = request.user

        serializer = PasswordChangeSerializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            old_password = serializer.data.get("old_password")
            if not user.check_password(old_password):
                return Response({"old_password": ["Eski şifre doğrulanmadı. Lütfen şifrenizi kontrol ediniz."]}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(serializer.data.get("password"))
            user.save()

            ur = UserRepository(user=user)
            new_token = ur.change_token()

            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # change_lost_password
    # şifre değiştirildiğinde token yenilenir. Tüm platformlarda sistemden çıkış yapılır
    @action(methods=['POST'], detail=False)
    def change_lost_password(self, request, *args, **kwargs):

        serializer = LostPasswordChangeSerializer(data=request.data)

        if serializer.is_valid():
            user = User.objects.filter(password_reset_token=serializer.data.get('code'), email=serializer.data.get('email')).first()

            if user:
                user.set_password(serializer.data.get('new_password'))
                user.password_reset_token = ""
                user.jwt_secret = uuid.uuid4()
                user.save()

                return Response(status=status.HTTP_200_OK)

            raise Http404

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # forgot password
    @action(methods=['POST'], detail=False)
    def forgot_password(self, request, *args, **kwargs):
        new_token = create_activate_token()
        user = User.objects.filter(email=request.data.get('email')).first()

        if user:
            user.password_reset_token = new_token
            user.save()

            send_mail(
                'Educate Şifre Hatırlatma Servisi',
                'Şifre yenileme kodunuz :  ' + str(new_token) + '\\r\\n Şifrenizi değiştirmek için <a href=\'http://link\'>tıklayın.</a>',
                'noreply@educate.com.tr',
                [user.email],
                fail_silently=True,
            )
            return Response(status=status.HTTP_200_OK)

        raise Http404

    # activate
    @action(methods=['POST'], detail=False)
    def activate_user(self, request, *args, **kwargs):
        user = User.objects.filter(register_email_activate_token=request.data.get('code'), email=request.data.get('email')).first()

        if user:
            user.is_active = 1
            user.save()

            return Response(status=status.HTTP_200_OK)

        raise Http404
