from rest_framework import permissions
from rest_framework.permissions import BasePermission


class CustomPermissionClass(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj
