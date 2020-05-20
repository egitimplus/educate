from django.db.models.signals import post_delete
from django.dispatch import receiver
from companies.models import SchoolLessonTeacher
from django.contrib.auth import get_user_model
from users.models import Role, Pattern
from django.contrib.contenttypes.models import ContentType
from companies.models import ClassroomTeacher, Classroom

User = get_user_model()

@receiver(post_delete, sender=SchoolLessonTeacher)
def delete_lesson_teacher_role(sender, instance, **kwargs):
    role_id = None
    user_teacher = ClassroomTeacher.objects.filter(teacher_id=instance.teacher_id).first()

    # Kullanıcının  rolünü silelim.
    if not user_teacher:
        check_role = Role.objects.filter(user_id=instance.teacher_id, group_id=7).first()

        if check_role:
            role_id = check_role.id
            check_role.delete()

    # Kullanıcının pattern rolünü silelim.
    # TODO burayı kontrol edelim SchoolLessonTeacher silmesi yapıyoruz.
    # TODO Neden Classroom kullandık ?
    role_classroom = Classroom.objects.get(id=instance.classroom_id)
    content_type_id = ContentType.objects.get_for_model(role_classroom).id
    Pattern.objects.filter(content_type_id=content_type_id, object_id=role_classroom.id, role_id=role_id).delete()
