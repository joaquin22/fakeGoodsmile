from rest_framework.permissions import BasePermission, SAFE_METHODS
from API.choices import UserTypeChoices


class IsAdminAuth(BasePermission):
    edit_methods = ("POST", "PUT", "PATCH")

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if request.user.is_authenticated:
            if request.user.user_type == UserTypeChoices.ADMIN:
                return True

        return False
