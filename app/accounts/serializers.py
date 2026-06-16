from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, data):
        user = User.objects.create_user(**data)
        Profile.objects.create(user=user)
        return user


class UserSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(source='profile.phone', required=False, allow_blank=True)
    address = serializers.CharField(source='profile.address', required=False, allow_blank=True)
    password = serializers.CharField(write_only=True, required=False, allow_blank=False, min_length=6)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff', 'phone', 'address', 'password')

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        password = validated_data.pop('password', None)
        for k, v in validated_data.items():
            setattr(instance, k, v)
        if password:
            instance.set_password(password)
        instance.save()
        profile, _ = Profile.objects.get_or_create(user=instance)
        for k, v in profile_data.items():
            setattr(profile, k, v)
        profile.save()
        return instance
