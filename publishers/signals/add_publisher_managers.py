from django.db.models.signals import post_save
from django.dispatch import receiver
from publishers.models import Publisher, PublisherManager
from django.http import Http404
from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save, sender=Publisher)
def add_publisher_managers(sender, created, instance, **kwargs):

    # Yayınevi kayıt edildikten sonra (post_save)
    if not created:

        if instance.add_manager:
            # yeni yöneticileri ekleyelim
            for user_id in instance.add_manager:
                try:
                    User.objects.get(id=user_id)
                except User.DoesNotExist:
                    raise Http404

                PublisherManager(manager_id=user_id, publisher_id=instance.id).save()

        # yeni listede olmayan mevcut yöneticileri silelim
        if instance.del_manager:
            PublisherManager.objects.filter(manager_id__in=instance.del_manager, publisher_id=instance.id).delete()

