from rest_framework import permissions
from django.utils.html import escape
from payments.models import UserProfile

class IsOwnerProfileOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_id==request.user

class IsAssociatedRecordOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method == 'PUT':
            login_user = request.user
            model_instance = UserProfile.objects.get(user_id=login_user)
            user_type = getattr(model_instance, 'user_type')
            # print(f'{user_type},{type(user_type)}')
            post_recipient_id = str(getattr(obj.recipient_id, 'id'))
            post_sender_id = str(getattr(obj.sender_id, 'id'))
            # print(f'recipient: {post_recipient_id}, post: {post_sender_id}')
            req_userid = str(request.user).split('.')[0]

            if user_type == "Hospital" and post_recipient_id==req_userid:
                print("return true in hospital")
                return True
            if user_type == "Company" and post_sender_id == req_userid:
                print("return true in company")
                return True
        return False
