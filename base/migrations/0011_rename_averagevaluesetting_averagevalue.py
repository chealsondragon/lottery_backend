# Generated by Django 4.2.2 on 2023-08-08 09:39

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0010_averagevaluesetting'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AverageValueSetting',
            new_name='AverageValue',
        ),
    ]
