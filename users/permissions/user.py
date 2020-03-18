from rest_framework.permissions import IsAuthenticated


class UserPermissionMixin(object):

    def get_permissions(self):

        group_object_permission_list = ['retrieve']

        if self.action in group_object_permission_list:

            permission_classes = [
                IsAuthenticated,
            ]

        else:
            permission_classes = []

        return [permission() for permission in permission_classes]

