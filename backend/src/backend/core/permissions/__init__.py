from rest_framework import permissions
from backend.core.types.user import UserTypes

class IsNotAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_authenticated

class IsSelf(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj

class IsSelfOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        is_self = request.user == obj
        is_admin = request.user.is_staff
        return is_self or is_admin
    
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        is_owner = obj.created_by == request.user
        is_admin = request.user.is_staff
        return is_owner or is_admin
    
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method not in permissions.SAFE_METHODS:
            return request.user.is_authenticated
        return True
    
    def has_object_permission(self, request, view, obj):
        if request.method not in permissions.SAFE_METHODS:
            return  obj.created_by == request.user
        return True
    
class IsCompanyUser(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.user_type == UserTypes.COMPANY.value
    
class IsStandardUser(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.user_type == UserTypes.STANDARD.value