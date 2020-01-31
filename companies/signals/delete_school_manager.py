from django.db.models.signals import post_delete
from django.dispatch import receiver
from companies.models import School, SchoolManager
from users.models import Role, Pattern
from django.contrib.contenttypes.models import ContentType


@receiver(post_delete, sender=SchoolManager)
def delete_school_manager_role(sender, instance, **kwargs):
    role_id = None
    user_manager = SchoolManager.objects.filter(manager_id=instance.manager_id).first()

    # Kullanıcının pattern rolünü silelim.
    if not user_manager:
        check_role = Role.objects.filter(user_id=instance.manager_id, group_id=9).first()

        if check_role:
            role_id = check_role.id
            check_role.delete()

    # Kullanıcının pattern rolünü silelim.
    role_school = School.objects.get(id=instance.school_id)
    content_type_id = ContentType.objects.get_for_model(role_school).id
    Pattern.objects.filter(content_type_id=content_type_id, object_id=role_school.id, role_id=role_id).delete()



