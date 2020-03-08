from rest_framework.permissions import BasePermission

from account.account_type import AccountType
from account.account_status import AccountStatus


class IsEmployer(BasePermission):
    """
    Allows access only to employers.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.type == AccountType.EMPLOYER.value)


class IsDefaultUser(BasePermission):
    """
    Allows access only to default users.
    """

class IsVerified(BasePermission):
    """
    Permission check for verification.
    """

    def has_permission(self, request, view):
        user = request.user
        return user and user.status == AccountStatus.VERIFIED.value
