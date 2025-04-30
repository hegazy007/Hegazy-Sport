from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from HegazyAPP import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Auth
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Main Pages
    path('', views.home, name='home'),
    path('teams/', views.teams, name='teams'),
    path('matches/', views.matches_view, name='matches'),
    path('matches/', views.matches_view, name='matches'),
    path('matches/', views.matches_view, name='matches'),
    path('match/<int:match_id>/', views.match_details, name='match_details'),
    path('matches/days/', views.today_and_tomorrow_matches, name='matches_days'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
