from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from companies.models import ClassroomTeacher, Classroom
from users.models import Role, Pattern
from django.contrib.contenttypes.models import ContentType


@receiver(pre_save, sender=ClassroomTeacher)
def add_classroom_teacher_role(sender, instance, **kwargs):
    # Sınıf öğretmeni eklenmeden önce (pre_save)
    # Daha önceden kullanıcıya öğretmen rolü eklenmiş mi bakalım. Eklenmediyse ekleyelim.
    check_role = Role.objects.filter(user_id=instance.teacher_id, group_id=7).first()

    if not check_role:
        add_role = Role(user_id=instance.teacher_id, group_id=7)
        add_role.save()

        role_id = add_role.id
    else:
        role_id = check_role.id

    # Öğretmenin ilgili sınıfta daha önceden aynı rolü yoksa yeni rolünü ekleyelim.
    role_classroom = Classroom.objects.get(id=instance.classroom_id)
    content_type_id = ContentType.objects.get_for_model(role_classroom).id
    Pattern.objects.get_or_create(content_type_id=content_type_id, object_id=role_classroom.id, role_id=role_id)
