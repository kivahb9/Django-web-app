# Generated by Django 2.2.1 on 2019-08-14 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20190814_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='tools',
            field=models.ManyToManyField(related_name='skillset', to='user.Tool'),
        ),
    ]
