# Generated by Django 2.2.1 on 2019-08-12 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20190812_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='tools',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='user.Tools'),
        ),
    ]
