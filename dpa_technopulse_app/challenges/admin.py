from django.contrib import admin
from .models import Challenges, UserChallenges, Comment, Project, UploadProject, Ranking

# Register your models here.

admin.site.register(Challenges)
admin.site.register(UserChallenges)
admin.site.register(Comment)
admin.site.register(UploadProject)
admin.site.register(Project)
admin.site.register(Ranking)
