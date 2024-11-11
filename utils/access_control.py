from rest_framework import permissions
from rest_framework.response import Response


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is the owner of the object
        permission_ok = obj.reviewer == request.user
        print("PERMISSION", permission_ok)
        if permission_ok is True:
            return permission_ok
        else:
            r = Response()
            r.status_code = 401
            r.data = {"success": False,
                      "message": "You don't have permission for this action"}
            return False
