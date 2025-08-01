# Generated by Django 5.2 on 2025-07-19 23:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_account_unique_code_per_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='account',
            name='unique_code_per_user',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='user',
            new_name='created_by',
        ),
        migrations.AddConstraint(
            model_name='account',
            constraint=models.UniqueConstraint(fields=('created_by', 'code'), name='unique_code_per_user'),
        ),
    ]
