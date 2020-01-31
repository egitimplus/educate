from django.db.models.signals import post_delete
from django.dispatch import receiver
from publishers.models import Publisher, PublisherManager
from users.models import Role, Pattern
from django.contrib.contenttypes.models import ContentType


@receiver(post_delete, sender=PublisherManager)
def delete_publisher_manager_role(sender, instance, **kwargs):
    role_id = None
    user_manager = PublisherManager.objects.filter(manager_id=instance.manager_id).first()

    # Kullanıcının pattern rolünü silelim.
    if not user_manager:
        check_role = Role.objects.filter(user_id=instance.manager_id, group_id=12).first()

        if check_role:
            role_id = check_role.id
            check_role.delete()

    # Kullanıcının pattern rolünü silelim.
    role_publisher = Publisher.objects.get(id=instance.publisher_id)
    content_type_id = ContentType.objects.get_for_model(role_publisher).id
    Pattern.objects.filter(content_type_id=content_type_id, object_id=role_publisher.id, role_id=role_id).delete()



