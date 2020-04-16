from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import os

# Create your models here.

"""
    
    The following models are, definitive source of information about the data &
    it contains essential fields and behaviors of the data that is being stored 
    in the database, where each model maps to a single database table.

"""


class Challenges(models.Model):
    challenge_name = models.CharField(max_length=50)
    challenge_inputfile = models.FileField()
    challenge_path = models.CharField(max_length=1000)
    challenge_description = models.TextField(default=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.challenge_name

    def get_absolute_url(self):
        return reverse("cha:challenges_view", args=[self.id])

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse("challenges_view", kwargs={"pk": self.pk})


class UserChallenges(models.Model):
    challenges = models.ForeignKey(Challenges, on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.challenges)

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        super().save(*args, **kwargs)

    @classmethod
    def create(cls, challenges_id, user_id):
        rev = cls(challenges=challenges_id, user=user_id)
        return rev


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    challenges = models.ForeignKey(Challenges, on_delete=models.PROTECT, null=True)
    content = models.TextField(max_length=200)
    reply = models.ForeignKey(
        "Comment", null=True, on_delete=models.PROTECT, related_name="replies"
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}-{}".format((self.challenges), str(self.user))

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        super().save(*args, **kwargs)


class Project(models.Model):
    project = models.CharField(max_length=50)
    created_date = models.DateTimeField(blank=True, editable=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.project

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        super().save(*args, **kwargs)


"""
    This function renames the Uploded file & saves it Uploaded_projects folder along with extension
"""


def content_file_name(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s_%s.%s" % (instance.user.id, instance.project.id, ext)
    return os.path.join("Uploaded_projects/", filename)


class UploadProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    details = models.TextField(max_length=2000)
    submission = models.FileField(upload_to=content_file_name)
    project = models.ForeignKey(
        Project, on_delete=models.PROTECT, null=True, default=Project
    )
    challenges = models.ForeignKey(Challenges, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        super().save(*args, **kwargs)


class Ranking(models.Model):
    developer_name = models.CharField(max_length=50)
    score = models.FloatField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "{}-{}".format((self.developer_name), str(self.score))

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        super().save(*args, **kwargs)

