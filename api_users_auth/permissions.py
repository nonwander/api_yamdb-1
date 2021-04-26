from rest_framework import permissions

from .models import CustomUser


class IsAuthorOrStaffOrReadOnly(permissions.BasePermission):
        def has_object_permission(self, request, view, obj):
            return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user
                or request.user.role == CustomUser.ROLE_ADMIN
                or request.user.role == 'moderator')


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )


class IsAdminRole(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_superuser or request.user.role==CustomUser.ROLE_ADMIN)
