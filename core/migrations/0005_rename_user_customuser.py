# Generated by Django 3.2.4 on 2022-01-28 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_user_user_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='CustomUser',
        ),
    ]
