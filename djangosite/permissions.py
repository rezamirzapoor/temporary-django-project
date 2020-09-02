from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    message = 'شما اجازه ویرایش یا حذف این آیتم را ندارید زیرا باید صاحب این آیتم باشید'
    def has_object_permission(self, request, view, obj):
        user = None
        try:
            user = request.user.getUser()
        except:
            user = None

        return obj.owner == None

class IsOwner(BasePermission):
    message = 'شما زیرا باید صاحب این آیتم باشید'
    def has_object_permission(self, request, view, obj):
        user = None
        try:
            user = request.user.getUser()
        except:
            user = None
            
        return obj.owner == request.user.getUser()