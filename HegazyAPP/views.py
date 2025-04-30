from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import Match, Team

def home(request):
    # اختيار المباريات التي ستُقام في المستقبل (بناءً على التاريخ)
    now = timezone.localtime()
    future_matches = Match.objects.filter(match_time__gt=now).order_by('match_time')

    # تمرير هذه المباريات للـ template
    return render(request, 'HegazyAPP/home.html', {'matches': future_matches})

def teams(request):
    all_teams = Team.objects.all()
    return render(request, 'HegazyAPP/teams.html', {'teams': all_teams})

def all_matches(request):
    all_matches = Match.objects.all().order_by('match_time')
    return render(request, 'HegazyAPP/matches.html', {'matches': all_matches})

def match_details(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    return render(request, 'HegazyAPP/match_details.html', {'match': match})

def matches_view(request):
    return render(request, 'HegazyAPP/matches.html')

def today_and_tomorrow_matches(request):
    now = timezone.localtime()
    today = now.date()
    tomorrow = today + timedelta(days=1)

    today_matches = Match.objects.filter(match_time__date=today).order_by('match_time')
    tomorrow_matches = Match.objects.filter(match_time__date=tomorrow).order_by('match_time')

    context = {
        'today_matches': today_matches,
        'tomorrow_matches': tomorrow_matches,
    }

    return render(request, 'HegazyAPP/matches_today_tomorrow.html', context)
