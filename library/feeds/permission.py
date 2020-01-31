from library.models import BackendPerms
from rest_framework import permissions


class GlobalPermissions(permissions.BasePermission):
    def has_permission(self, request, view):

        view_name = view.__class__.__name__
        perms = BackendPerms.objects.filter(view_name=view_name, view_action=view.action).all()
        perm_list = []
        for item in perms:
            perm_list.append(item.permission_name)

        return request.user.has_perms(perm_list)
