# Generated by Django 3.0.3 on 2020-06-03 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django_etebase.token_auth import models as token_auth_models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AuthToken",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "key",
                    models.CharField(db_index=True, default=token_auth_models.generate_key, max_length=40, unique=True),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("expiry", models.DateTimeField(blank=True, default=token_auth_models.get_default_expiry, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="auth_token_set",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]