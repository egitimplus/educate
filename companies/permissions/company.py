from rest_framework.permissions import IsAuthenticated, IsAdminUser
from library.feeds import GlobalPermissions
from .object_permissions import GroupObjectPermission


class GroupPermissionMixin(object):

    def get_permissions(self):

        group_object_permission_list = ['retrieve', 'destroy', 'update', 'school_list', 'publisher_list']
        admin_permission_list = ['list', 'create']

        if self.action in group_object_permission_list:

            permission_classes = [
                IsAuthenticated,
                GlobalPermissions,
                GroupObjectPermission
            ]
        elif self.action in admin_permission_list:

            permission_classes = [
                IsAdminUser,
                GlobalPermissions,
            ]
        else:
            permission_classes = [
                IsAuthenticated,
                GlobalPermissions
            ]
        permission_classes = []
        return [permission() for permission in permission_classes]

