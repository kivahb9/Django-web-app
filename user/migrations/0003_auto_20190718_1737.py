# Generated by Django 2.2.1 on 2019-07-18 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_bachelorsdegree_challenges_gender_graduationyear_signupregistration_skill_state_subscriber_userchall'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userchallenges',
            name='challenges',
        ),
        migrations.RemoveField(
            model_name='userchallenges',
            name='user',
        ),
        migrations.DeleteModel(
            name='Challenges',
        ),
        migrations.DeleteModel(
            name='UserChallenges',
        ),
    ]
