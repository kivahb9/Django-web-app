from django.contrib import admin
from django.contrib.admin import widgets
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ManyToManyWidget
from import_export import resources, fields
from django.contrib.auth.forms import PasswordResetForm
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from .models import (
    Profile,
    BachelorsDegree,
    State,
    GraduationYear,
    SignUpRegistration,
    Gender,
    Tool,
    Skill,
)
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.http import HttpResponse, BadHeaderError
from .forms import UserCreationForm, SkillForm, SignUpRegistrationForm

# ------------------------------------------------------------------------------------------------------------
# Import-Export module with custom mapping to the foreign key field from a different table
class UserResourse(resources.ModelResource):
    # groups = fields.Field(
    #     attribute= 'groups',
    #     widget=ManyToManyWidget(Group, separator='|', field='name'))

    class Meta:
        model = User
        exclude = (
            "id",
            "last_login",
            "is_superuser",
            "user_permissions",
            "date_joined",
            "is_active",
            "groups",
        )
        import_id_fields = (
            "password",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
        )


# custom admin class for the User model, subclassing Django's one
class UserProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


# Registering ImportExportModel to admin site and also tweaking the default look and feel. Adding custom search, ordering, filtering etc.
class UserAdmin(ImportExportModelAdmin, UserAdmin, admin.ModelAdmin):
    resource_class = UserResourse
    add_form = UserCreationForm
    inlines = (UserProfileInline,)
    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                ),
                "classes": ("wide",),
            },
        ),
    )

    def save_model(self, request, obj, form, change):
        if not change and (
            not form.cleaned_data["password1"] or not obj.has_usable_password()
        ):
            # Django's PasswordResetForm won't let us reset an unusable
            # password. We set it above super() so we don't have to save twice.
            obj.set_password(get_random_string())
            reset_password = True
        else:
            reset_password = False

        super(UserAdmin, self).save_model(request, obj, form, change)
        try:
            # To send welcome email to all the user created using Django Admin
            if reset_password:
                reset_form = PasswordResetForm({"email": obj.email})

                # Get all the details from the insert
                Context = {
                    "first_name": obj.first_name,
                    "last_name": obj.last_name,
                    "email": obj.email,
                    "username": obj.username,
                }
                assert reset_form.is_valid()
                reset_form.save(
                    request=request,
                    use_https=request.is_secure(),
                    subject_template_name="user/account_creation_subject.txt",
                    html_email_template_name="user/welcome.html",
                    extra_email_context=Context,
                )
        except BadHeaderError:
            return HttpResponse("Invalid header found.")


class MyAdmin(admin.ModelAdmin):
    form = SkillForm

class SignAdmin(admin.ModelAdmin):
    form = SignUpRegistrationForm
# ------------------------------------------------------------------------------------------------------------

# Django Admin Page header name
admin.site.site_header = "TechnoPulse Administrator System"
admin.site.site_title = "TechnoPulse Admin Portal"
admin.site.index_title = "Welcome to TechnoPulse Admin Portal"

# Unregistering user model and then registering the same with customisation.
admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), UserAdmin)
admin.site.register(Gender)
admin.site.register(GraduationYear)
admin.site.register(State)
admin.site.register(BachelorsDegree)
admin.site.register(SignUpRegistration,SignAdmin)
admin.site.register(Tool)
admin.site.register(Skill, MyAdmin)
