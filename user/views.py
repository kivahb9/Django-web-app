from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth import login
from django.views.generic import CreateView, UpdateView
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import views as auth_views
from .forms import UserRegisterForm, SubscriberForm, SignUpRegistrationForm, SkillForm
from .models import Subscriber, SignUpRegistration, Skill
from .models import Profile
from django.views.generic import FormView
from challenges.models import Challenges
from django.contrib.auth.mixins import LoginRequiredMixin

# from django.contrib.auth import get_user_model


"""
    This function displays message or rather pops notification of account being created

    Parameters:
    Null

    Returns:
    It checks whether the form which being passed in the HTML template is valid or not on basis
    of which the message is displayed

"""


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            return redirect("signupregistration")
    else:
        form = UserRegisterForm()

    return render(request, "user/register.html", {"form": form})


"""
    This function displays message or rather pops notification on updation of account.

    Parameters:
    Null

    Returns:
    It checks whether the form which being passed in the HTML template is valid or not on basis
    of which the message is displayed

"""


@login_required
def profile(request):
    if request.method == "POST":
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )

        if p_form.is_valid():
            p_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect("profile")
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {"p_form": p_form}

    return render(request, "user/profile.html", context)


"""
    This function is used for rendering particular template

    Parameters:
    Null
"""


@login_required
def home(request):
    context = {}
    return render(request, "user/profile.html", context)


"""
    This function displays message or rather pops notification for subscribing to a newsletter.

    Parameters:
    Null

    Returns:
    It checks whether the form which being passed in the HTML template is valid or not on basis
    of which the message is displayed on its exsistance in the database
"""


def subscribe(request):
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if Subscriber.objects.filter(email=instance.email).exists():
                messages.warning(
                    request, "You have already subscribed to our notifications"
                )
            else:
                instance.save()

                messages.success(
                    request,
                    "You have successfully subscribed to recieve futhur notifications on technopulse hackathon",
                )

            return redirect("technopulse_home")
    else:
        form = SubscriberForm()
    return render(request, "user/index.html", {"form": form})


"""
    Class based Skillview renders template name & then it checks if the information entered in the form 
    is correct or not and then passes onto Success URL where it aslo checks whether the user is
    authenticated or not.
    
    Parameters:
    Null
    
    Returns:
    Template_name
"""


class Skillview(LoginRequiredMixin, CreateView):
    template_name = "user/skill.html"
    model = Skill
    success_url = reverse_lazy("cha:challenge")

    fields = [
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

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super(Skillview, self).form_valid(form)


"""
    Class based SignUpRegistrationCreateView renders template name & then it checks if 
    the information entered in the form is correct or not and then passes onto Success 
    URL where it aslo checks whether the user is authenticated or not.

    Parameters:
    Null

    Returns:
    Template_name
"""


class SignUpRegistrationCreateView(LoginRequiredMixin, CreateView):
    template_name = "user/signupregistration.html"
    model = SignUpRegistration
    success_url = reverse_lazy("skill")

    fields = [
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

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super(SignUpRegistrationCreateView, self).form_valid(form)

