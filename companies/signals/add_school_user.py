from django.db.models.signals import post_save
from django.dispatch import receiver
from companies.models import SchoolManager, SchoolUser


@receiver(post_save, sender=SchoolManager)
def add_school_user(sender, created, instance, **kwargs):

    if created:
        SchoolUser.objects.get_or_create(school_id=instance.school_id, user_id=instance.manager_id)
