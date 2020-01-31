from django.db.models.signals import post_save
from django.dispatch import receiver
from companies.models import SchoolLessonTeacher
from django.contrib.auth import get_user_model
from users.models import Role, Pattern
from django.contrib.contenttypes.models import ContentType

User = get_user_model()


@receiver(post_save, sender=SchoolLessonTeacher)
def add_lesson_teacher_role(sender, instance, **kwargs):
    # Ders öğretmeni eklenmeden önce (pre_save)
    # Daha önceden kullanıcıya öğretmen rolü eklenmiş mi bakalım. Eklenmediyse ekleyelim.

    find_user = instance.teacher.teacher.id

    check_role = Role.objects.filter(user_id=find_user, group_id=6).first()

    if not check_role:
        add_role = Role(user_id=find_user, group_id=6)
        add_role.save()

        role_id = add_role.id
    else:
        role_id = check_role.id

    # Öğretmenin ilgili derse daha önceden aynı rolü yoksa yeni rolünü ekleyelim.
    role_lesson = SchoolLessonTeacher.objects.get(id=instance.id)
    content_type_id = ContentType.objects.get_for_model(role_lesson).id
    Pattern.objects.get_or_create(content_type_id=content_type_id, object_id=instance.id, role_id=role_id)
