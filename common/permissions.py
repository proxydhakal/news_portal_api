from rest_framework import permissions
from apps.accounts.models import User

class IsAdminOrJournalist(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            return str(request.user.role) in [role for role, name in User.ROLES if name in ['Admin','Journalist']]
        except Exception as e:
            return False
        
class UserIsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS and obj.id == request.user.id