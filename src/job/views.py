from django.shortcuts import render

from rest_framework.permissions import BasePermission

from account.account_status import AccountStatus

class IsVerified(BasePermission):
    """
    Permission check for verification.
    """

    def has_permission(self, request, view):
        return request.user.status == AccountStatus.VERIFIED.value

# Create your views here.
