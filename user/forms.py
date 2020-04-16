from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Subscriber, SignUpRegistration, Skill, Tool


"""
    Django forms are used to accquire GET or POST data from various HTML template,
    where ther fields are accessed from their respective models which works as
    end-to-end working collection of these parts to the Django Form class
"""


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ["email"]


class SignUpRegistrationForm(forms.ModelForm):
    experience = forms.ChoiceField(choices=[(x, x) for x in range(1, 100)])

    class meta:
        model = SignUpRegistration
        fields = [
            "experience",
            "gender",
            "city",
            "institute",
            "graduation_year",
            "bachelors_degree",
            "experience",
            "company",
            "job_title",
            "state",
            "resume",
            "agreement",
        ]


class SkillForm(forms.ModelForm):
    tools = forms.ModelMultipleChoiceField(
        queryset=Tool.objects.all(), required=False, widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Skill
        fields = [
            "user",
            "tools",
            "backend_development",
            "frontend_development",
            "network_architecture",
            "android_development",
            "iOS_development",
            "system_administration",
            "quality_assurance",
            "data_architecture",
            "game_design_development",
            "network_security",
            "information_security",
            "erp",
            "design_engineering",
            "graphic_designing",
            "ux",
        ]

