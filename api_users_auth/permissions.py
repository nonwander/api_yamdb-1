from rest_framework import permissions

from .models import CustomUser


class IsAuthorOrStaffOrReadOnly(permissions.BasePermission):
        def has_object_permission(self, request, view, obj):
            return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user
                or request.user.is_admin
                or request.user.is_moderator)
"""

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_admin
            or request.user.is_superuser
        )
"""

class IsSuperuser(permissions.BasePermission):

    def has_permission(self, request, view):
        return (request.user.is_superuser)


class IsAdminRole(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return request.user.is_staff
        return (request.user.is_superuser
            or request.user.is_admin
    )

"""    
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.is_admin
 
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin

    def has_delete_permission(self, request):
        if request.user.is_admin:
            return False
 
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
"""