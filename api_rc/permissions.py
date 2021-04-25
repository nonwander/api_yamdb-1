from rest_framework import permissions

from .models import Roles

MODERATOR_METHODS = ('PATCH', 'DELETE')


class ReviewCommentPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'POST':
            return not request.user.is_anonymous()

        if request.method in MODERATOR_METHODS:
            return (
                request.user == obj.author
                or request.user.role == Roles.ADMIN
                or request.user.role == Roles.MODERATOR
            )

        return request.method in permissions.SAFE_METHODS