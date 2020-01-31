from django.db.models.signals import post_delete
from django.dispatch import receiver
from companies.models import ClassroomLesson
from users.models import Role, Pattern
from django.contrib.contenttypes.models import ContentType

@receiver(post_delete, sender=ClassroomLesson)
def delete_classroom_lesson_role(sender, instance, **kwargs):

    # aynı öğretmenin başka özel dersi varmı bulalım
    model = ContentType.objects.get_for_model(ClassroomLesson)
    model_id = model.id

    find_user = instance.lesson.teacher.teacher.id

    role = Role.objects.filter(user_id=find_user, group_id=6).first()

    patterns = Pattern.objects.filter(content_type_id=model_id, role_id=role.id).count()

    if patterns == 1:
        Role.objects.filter(user_id=find_user, group_id=6).delete()

    Pattern.objects.filter(content_type_id=model_id, object_id=instance.classroom_id, role_id=role.id).delete()

