from django.db.models.signals import pre_save
from django.dispatch import receiver
from publishers.models import Publisher, PublisherManager
from users.models import Role, Pattern
from django.contrib.contenttypes.models import ContentType


@receiver(pre_save, sender=PublisherManager)
def add_publisher_manager_role(sender, instance, **kwargs):

    # Yayınevi yöneticisi eklenmeden önce (pre_save)
    # Daha önceden kullanıcıya yönetici rolü eklenmiş mi bakalım. Eklenmediyse ekleyelim.
    check_role = Role.objects.filter(user_id=instance.manager_id, group_id=12).first()

    if not check_role:
        add_role = Role(user_id=instance.manager_id, group_id=12)
        add_role.save()

        role_id = add_role.id
    else:
        role_id = check_role.id

    # Kullanıcının ilgili olulda daha önceden aynı rolü yoksa yeni rolünü ekleyelim.
    role_publisher = Publisher.objects.get(id=instance.publisher_id)
    content_type_id = ContentType.objects.get_for_model(role_publisher).id
    Pattern.objects.get_or_create(content_type_id=content_type_id, object_id=role_publisher.id, role_id=role_id)