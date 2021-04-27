from rest_framework import permissions

from api_users_auth.models import CustomUser

MODERATOR_METHODS = ('PATCH', 'DELETE')


class ReviewCommentPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'POST':
            return not request.user.is_anonymous()

        if request.method in MODERATOR_METHODS:
            return (
                request.user == obj.author
                or request.user.role == CustomUser.ROLE_ADMIN
                or request.user.role == CustomUser.ROLE_MODERATOR
            )

        return request.method in permissions.SAFE_METHODS