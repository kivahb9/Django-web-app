# Generated by Django 2.2.1 on 2019-08-14 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20190814_1256'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='tool',
            new_name='tools',
        ),
    ]
