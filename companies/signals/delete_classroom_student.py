from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from companies.models import Classroom, ClassroomStudent
from users.models import Role, Pattern
from django.contrib.contenttypes.models import ContentType


@receiver(post_delete, sender=ClassroomStudent)
def delete_classroom_student_role(sender, instance, **kwargs):
    role_id = None
    user_teacher = ClassroomStudent.objects.filter(student_id=instance.student_id).first()

    # Kullanıcının pattern rolünü silelim.
    if not user_teacher:
        check_role = Role.objects.filter(user_id=instance.student_id, group_id=3).first()

        if check_role:
            role_id = check_role.id
            check_role.delete()

    # Kullanıcının pattern rolünü silelim.
    role_classroom = Classroom.objects.get(id=instance.classroom_id)
    content_type_id = ContentType.objects.get_for_model(role_classroom).id
    Pattern.objects.filter(content_type_id=content_type_id, object_id=role_classroom.id, role_id=role_id).delete()