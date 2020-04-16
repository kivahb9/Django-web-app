import os
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Challenges, UserChallenges, Comment, UploadProject, Ranking
from .forms import ChallengesForm, UserChallengesForm, CommentForm, UploadProjectForm
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse
from django.urls import reverse_lazy


""" 
    Below functions displays all the challenges present in the hackathon which is
    being displayed dynamically with the help of their respective id's
   
    Parameters:
    Null

    Returns: 
    This is done by getting all the objects present in the model Challenges which
    in turn would display all the parameters across the HTML.
  
"""


@login_required
def challenges_list_view(request):
    context = {}
    try:
        challenges = Challenges.objects.all()
    except:
        return "challenge"
    context = {"challenges": challenges}
    return render(request, "challenges/challenge.html", context)


"""
    This function is called for getting a detailed view for each challenge which
    would display all the required details of a challenge to get started.
 
    Parameters:
    id(int): set to none

    Returns:
    All the deatils consisting in a particular challenge are rendered through 
    database with the help of model Challenge & this function is also used for
    creating a discussion forum which includes comments & replies which are dynamical
    as the challenges changes.
 
"""


@login_required
def challenges_detail_view(request, id=None):
    context = {}
    challenge = Challenges.objects.get(id=id)
    challenges = get_object_or_404(Challenges, id=id)
    comments = Comment.objects.filter(challenges=challenges, reply=None).order_by("-id")
    if request.method == "POST":
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get("content")
            reply_id = request.POST.get("comment_id")
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(
                challenges=challenges,
                user=request.user,
                content=content,
                reply=comment_qs,
            )
            comment.save()
            return HttpResponseRedirect(challenges.get_absolute_url())

    else:

        comment_form = CommentForm()
    context = {
        "challenge": challenge,
        "comments": comments,
        "comment_form": comment_form,
    }
    return render(request, "challenges/challenges_view.html", context)


"""
    This function is built to get rendered in challenges_detail_view function

    Parameters:
    Null
"""


def get_absolute_url(self):
    return reverse("challenges.views.challenges_detail_view", args=[str(self.id)])


"""
    Register function is created in order to know how many users have registered 
    for a particular challenge

    Over here the concept of GET have been used & data is accquired through URL
    variable U & C gets the instance from the model since they are foreign keys,
    and are assigned to the objects in UserChallenge model; secondly if condition 
    is created which checks whether user have registered for the challenge or not &
    accordingly displays message.

    Parameters:
    id(int): set to none
"""


def register(request=None, id=None):
    challenges = Challenges.objects.get(id=id)
    user = request.GET.get("ytrewq")
    challenge = request.GET.get("qwerty")
    U = User.objects.get(id__exact=user)
    C = Challenges.objects.get(id__exact=challenge)
    userchallenges_instance = UserChallenges(challenges=C, user=U)
    userchallenges_instance.save()
    if UserChallenges.objects.filter(user=user, challenges=challenges).exists():
        messages.warning(request, "You have already registered to this challenge")
    else:
        messages.success(
            request,
            "You have successfully subscribed to recieve futhur notifications on technopulse hackathon",
        )
    return HttpResponseRedirect(challenges.get_absolute_url())


"""
    Download function is placed on the challenge page inside the download file section

    Parameters:
    ChallengesName(string): File name which consist of download able files  

    Returns:
    The files which will be made available for download across each challenge is extracted 
    through a folder named ChallengesName inside media & will respond dynamically as the 
    challenge changes
"""


def download(request, ChallengesName):
    response = HttpResponse(mimetype="application/force-download")
    response["Content-Disposition"] = "attachment; ChallengesName=%s" % smart_str(
        ChallengesName
    )
    response["X-Sendfile"] = smart_str(settings.MEDIA_ROOT + ChallengesName)
    return HttpResponse("challenges_view.html")


"""
    This function is a class based view which checks whether uploaded file is vaild or not

    Parameters:
    Null

    Returns:
    The files which will be uploaded checks wether all feilds are filled or not and is 
    accordingly passed on to success URL
"""


class UploadProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = "challenges/uploadproject.html"
    model = UploadProject
    success_url = reverse_lazy("cha:challenge")
    fields = ["details", "submission", "project"]

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super(UploadProjectCreateView, self).form_valid(form)


"""
    This function is built to get display the results 
    Parameters:
    Null
"""


class RankingListView(ListView):
    template_name = "challenges/result.html"

    def get_queryset(self):
        return Ranking.objects.all()

