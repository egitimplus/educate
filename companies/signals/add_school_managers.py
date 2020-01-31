from django.db.models.signals import post_save
from django.dispatch import receiver
from companies.models import School, SchoolManager
from django.http import Http404
from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save, sender=School)
def add_school_managers(sender, created, instance, **kwargs):

    # Okul kayıt edildikten sonra (post_save)
    if not created:

        if instance.add_manager:
            # yeni yöneticileri ekleyelim
            for user_id in instance.add_manager:
                try:
                    User.objects.get(id=user_id)
                except User.DoesNotExist:
                    raise Http404

                SchoolManager(manager_id=user_id, school_id=instance.id).save()

        # yeni listede olmayan mevcut yöneticileri silelim
        if instance.del_manager:
            SchoolManager.objects.filter(manager_id__in=instance.del_manager, school_id=instance.id).delete()

