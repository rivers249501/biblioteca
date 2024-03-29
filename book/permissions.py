from rest_framework import permissions


class IsOwnerOrReadOnlyBook(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_superuser or request.user.is_staff:
            return True

        return obj.owner == request.user 