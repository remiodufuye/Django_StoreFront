
from rest_framework import permissions

class isAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request,view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)
    pass 


class FullDjangoModelPermissions(permissions.DjangoModelPermissions):
    def __init__(self) -> None:
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']
    pass 


class ViewCustomerHistoryPermission(permissions.BasePermission):
    def has_permission(self, request,view):
        return request.user.has_perm('store.view_history')
    