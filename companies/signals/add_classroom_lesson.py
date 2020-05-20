from django.db.models.signals import post_save
from django.dispatch import receiver
from companies.models import ClassroomLesson
from users.models import Role, Pattern
from django.contrib.contenttypes.models import ContentType


@receiver(post_save, sender=ClassroomLesson)
def add_classroom_lesson_role(sender, instance, **kwargs):
    model = ContentType.objects.get_for_model(ClassroomLesson)
    model_id = model.id

    find_user = instance.lesson.teacher.teacher.id
    check_role = Role.objects.filter(user_id=find_user, group_id=6).first()

    if not check_role:
        add_role = Role(user_id=find_user, group_id=6)
        add_role.save()

        role_id = add_role.id
    else:
        role_id = check_role.id

    Pattern.objects.get_or_create(content_type_id=model_id, object_id=instance.id, role_id=role_id)
