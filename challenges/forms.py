from django import forms
from django.contrib.auth.models import User
from .models import Challenges, UserChallenges, Comment, UploadProject

"""
    Django forms are used to accquire GET or POST data from various HTML template,
    where ther fields are accessed from their respective models which works as
    end-to-end working collection of these parts to the Django Form class
"""


class ChallengesForm(forms.ModelForm):
    class Meta:
        model = Challenges
        fields = ["challenge_name", "challenge_inputfile"]


class UserChallengesForm(forms.ModelForm):
    class Meta:
        model = UserChallenges
        fields = ["user", "challenges"]


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Type your message here...",
                "rows": "6",
            }
        ),
    )

    class Meta:
        model = Comment
        fields = ["content"]


class UploadProjectForm(forms.ModelForm):
    class Meta:
        model = UploadProject
        fields = ["details", "submission", "project"]

