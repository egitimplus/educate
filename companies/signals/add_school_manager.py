from django.db.models.signals import pre_save
from django.dispatch import receiver
from companies.models import School, SchoolManager
from users.models import Role, Pattern
from django.contrib.contenttypes.models import ContentType


@receiver(pre_save, sender=SchoolManager)
def add_school_manager_role(sender, instance, **kwargs):

    # Okul yöneticisi eklenmeden önce (pre_save)
    # Daha önceden kullanıcıya yönetici rolü eklenmiş mi bakalım. Eklenmediyse ekleyelim.
    check_role = Role.objects.filter(user_id=instance.manager_id, group_id=9).first()

    if not check_role:
        add_role = Role(user_id=instance.manager_id, group_id=9)
        add_role.save()

        role_id = add_role.id
    else:
        role_id = check_role.id

    # Kullanıcının ilgili olulda daha önceden aynı rolü yoksa yeni rolünü ekleyelim.
    role_school = School.objects.get(id=instance.school_id)
    content_type_id = ContentType.objects.get_for_model(role_school).id
    Pattern.objects.get_or_create(content_type_id=content_type_id, object_id=role_school.id, role_id=role_id)
