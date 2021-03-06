# Generated by Django 2.2.1 on 2019-07-18 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BachelorsDegree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree_name', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(blank=True, editable=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Challenges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challenge_name', models.CharField(max_length=50)),
                ('challenge_inputfile', models.FileField(upload_to='')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(blank=True, editable=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='GraduationYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('created_date', models.DateTimeField(blank=True, editable=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(blank=True, editable=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('created_date', models.DateTimeField(blank=True, editable=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserChallenges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_date', models.DateTimeField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('challenges', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='user.Challenges')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('framework', models.CharField(max_length=200)),
                ('backend_development', models.BooleanField(default=False)),
                ('frontend_development', models.BooleanField(default=False)),
                ('network_architecture', models.BooleanField(default=False)),
                ('android_development', models.BooleanField(default=False)),
                ('iOS_development', models.BooleanField(default=False)),
                ('system_administration', models.BooleanField(default=False)),
                ('quality_assurance', models.BooleanField(default=False)),
                ('data_architecture', models.BooleanField(default=False)),
                ('game_design_development', models.BooleanField(default=False)),
                ('network_security', models.BooleanField(default=False)),
                ('information_security', models.BooleanField(default=False)),
                ('erp', models.BooleanField(default=False)),
                ('design_engineering', models.BooleanField(default=False)),
                ('ux', models.BooleanField(default=False)),
                ('graphic_designing', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SignUpRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('institute', models.CharField(default='', max_length=100)),
                ('experience', models.IntegerField()),
                ('company', models.CharField(max_length=50)),
                ('job_title', models.CharField(max_length=30)),
                ('resume', models.FileField(upload_to='')),
                ('created_date', models.DateTimeField(blank=True, editable=False, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('agreement', models.BooleanField(default=False)),
                ('bachelors_degree', models.ForeignKey(default=user.models.BachelorsDegree, null=True, on_delete=django.db.models.deletion.PROTECT, to='user.BachelorsDegree')),
                ('gender', models.ForeignKey(default=user.models.Gender, null=True, on_delete=django.db.models.deletion.PROTECT, to='user.Gender')),
                ('graduation_year', models.ForeignKey(default=user.models.GraduationYear, null=True, on_delete=django.db.models.deletion.PROTECT, to='user.GraduationYear')),
                ('state', models.ForeignKey(default=user.models.State, null=True, on_delete=django.db.models.deletion.PROTECT, to='user.State')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
