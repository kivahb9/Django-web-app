from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from multiselectfield import MultiSelectField

"""

    The following models are, definitive source of information about the data &
    it contains essential fields and behaviors of the data that is being stored
    in the database, where each model maps to a single database table.

"""


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")
    created_date = models.DateTimeField(blank=True, editable=False)
    updated_date = models.DateTimeField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} profile"

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Subscriber(models.Model):
    email = models.EmailField()
    created_date = models.DateTimeField(blank=True, editable=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        super().save(*args, **kwargs)


class Gender(models.Model):
    gender = models.CharField(max_length=50)
    created_date = models.DateTimeField(blank=True, editable=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.gender

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        super().save(*args, **kwargs)


class GraduationYear(models.Model):
    year = models.IntegerField()
    created_date = models.DateTimeField(blank=True, editable=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.year}"

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        super().save(*args, **kwargs)


class BachelorsDegree(models.Model):
    degree_name = models.CharField(max_length=50)
    created_date = models.DateTimeField(blank=True, editable=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.degree_name

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        super().save(*args, **kwargs)


class State(models.Model):
    state_name = models.CharField(max_length=50)
    created_date = models.DateTimeField(blank=True, editable=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.state_name

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        super().save(*args, **kwargs)


class SignUpRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    gender = models.ForeignKey(
        Gender, on_delete=models.PROTECT, null=True, default=Gender
    )
    city = models.CharField(max_length=50)
    institute = models.CharField(max_length=100, default="")
    graduation_year = models.ForeignKey(
        GraduationYear, on_delete=models.PROTECT, null=True, default=GraduationYear
    )
    bachelors_degree = models.ForeignKey(
        BachelorsDegree, on_delete=models.PROTECT, null=True, default=BachelorsDegree
    )
    experience = models.FloatField(range(1, 100))
    company = models.CharField(max_length=50)
    job_title = models.CharField(max_length=30)
    state = models.ForeignKey(State, on_delete=models.PROTECT, null=True, default=State)
    resume = models.FileField()
    created_date = models.DateTimeField(blank=True, null=True, editable=False)
    is_active = models.BooleanField(default=True)
    agreement = models.BooleanField(default=False, blank=False, null=False)

    def __str__(self):
        return self.user

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        super().save(*args, **kwargs)


class Tool(models.Model):
    tools = models.CharField(max_length=100)

    def __str__(self):
        return self.tools

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        super().save(*args, **kwargs)


class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tools = models.ManyToManyField(Tool, related_name="skillset")
    backend_development = models.BooleanField(default=False)
    frontend_development = models.BooleanField(default=False)
    network_architecture = models.BooleanField(default=False)
    android_development = models.BooleanField(default=False)
    iOS_development = models.BooleanField(default=False)
    system_administration = models.BooleanField(default=False)
    quality_assurance = models.BooleanField(default=False)
    data_architecture = models.BooleanField(default=False)
    game_design_development = models.BooleanField(default=False)
    network_security = models.BooleanField(default=False)
    information_security = models.BooleanField(default=False)
    erp = models.BooleanField(default=False)
    design_engineering = models.BooleanField(default=False)
    ux = models.BooleanField(default=False)
    graphic_designing = models.BooleanField(default=False)

    def __str__(self):
        return self.user

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        super().save(*args, **kwargs)
