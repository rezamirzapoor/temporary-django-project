from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from .models import User
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.hashers import make_password

class UserListSerializer(ModelSerializer):
    detail_url = HyperlinkedIdentityField(view_name="user-detail")
    class Meta:
        model = User
        fields = [
            'id',
            'is_superuser',
            'email',
            'name',
            'avatar',
            'is_active',
            'is_staff',
            'groups',
            'detail_url'
        ]

class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['favorite_blogs']

class UserCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'is_superuser',
            'email',
            'name',
            'avatar',
            'is_active',
            'is_staff',
            'groups'
        ]

class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'name',
            'password'
        ]
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
    
class PermissionSerializer(ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'
        depth = 1


class GroupListSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        depth = 1

class GroupCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = [
            'name',
            'permissions'
        ]
        depth = 1
