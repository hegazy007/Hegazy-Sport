from django.contrib import admin
from HegazyAPP.models import Match

# Register your models here.

class Matchadmin(admin.ModelAdmin):

        list_display = ['home_team', 'away_team', 'match_time','location','home_score','away_score','status',]


admin.site.register(Match, Matchadmin)