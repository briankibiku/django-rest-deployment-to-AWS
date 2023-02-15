from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own permissions"""

    def has_object_permission(self, request, view, obj):
        """check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """allow users to update own status"""

    def has_object_permission(self, request, view, obj):
        """check if user is editing their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id