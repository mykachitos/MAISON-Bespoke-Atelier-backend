import os

from django.apps import AppConfig
from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate


def bootstrap_superuser(**_kwargs):
    username = os.getenv('DJANGO_SUPERUSER_USERNAME')
    password = os.getenv('DJANGO_SUPERUSER_PASSWORD')
    email = os.getenv('DJANGO_SUPERUSER_EMAIL', '')

    if not username or not password:
        return

    user_model = get_user_model()
    user, created = user_model.objects.get_or_create(
        username=username,
        defaults={
            'email': email,
            'is_staff': True,
            'is_superuser': True,
        },
    )

    should_save = False

    if created:
        user.set_password(password)
        should_save = True

    if email and user.email != email:
        user.email = email
        should_save = True

    if not user.is_staff:
        user.is_staff = True
        should_save = True

    if not user.is_superuser:
        user.is_superuser = True
        should_save = True

    if should_save:
        user.save()


class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        post_migrate.connect(bootstrap_superuser, sender=self, dispatch_uid='accounts.bootstrap_superuser')
