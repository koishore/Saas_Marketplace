# Generated by Django 3.2.4 on 2022-01-28 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_user_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='seller_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
