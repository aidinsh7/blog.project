from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user or request.IsSuperUser)


class IsStaffOrReadonly(BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS or
        request.user and 
        request.IsStaffOrReadonly)



class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
         return True
        return bool(request.user.is_authenticated and request.user.IsSuperUser or  obj.auther == request.user)




class IsSuperUserOrStaffReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool (request.method in SAFE_METHODS and 
        request.user and 
        request.user.is_staff and 
        request.user and 
        request.user.is_superuser)
