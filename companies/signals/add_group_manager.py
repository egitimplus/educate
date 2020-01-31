from django.db.models.signals import post_save
from django.dispatch import receiver
from companies.models import CompanyGroup
from django.contrib.auth import get_user_model
from users.models import Role, Pattern
from django.contrib.contenttypes.models import ContentType

User = get_user_model()


@receiver(post_save, sender=CompanyGroup)
def add_group_manager_role(sender, created, instance, **kwargs):

    # Grup kayıt edildikten sonra (post_save)
    if created:
        # Daha önceden kullanıcıya yönetici rolü eklenmiş mi bakalım. Eklenmediyse ekleyelim.
        check_role = Role.objects.filter(user_id=instance.user_id, group_id=13).first()

        if not check_role:
            add_role = Role(user_id=instance.user_id, group_id=13)
            add_role.save()

            role_id = add_role.id
        else:
            role_id = check_role.id

        # Kullanıcının ilgili olulda daha önceden aynı rolü yoksa yeni rolünü ekleyelim.
        role_group = CompanyGroup.objects.get(id=instance.id)
        content_type_id = ContentType.objects.get_for_model(role_group).id
        Pattern.objects.get_or_create(content_type_id=content_type_id, object_id=instance.id, role_id=role_id)

