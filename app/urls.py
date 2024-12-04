from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.intro_video, name='intro_video'),  # Homepage for the video
    path('login/', views.login_view, name='login'),  # Login page
    path('register/', views.register_view, name='register'),  # Registration page
    path('logout/', views.logout_view, name='logout'),  # Logout functionality

    path('home/', views.home_view, name='home'),  # Home page
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard

    path('mentor/', views.mentor, name='mentor'),  # General Mentor page
    path('career_mentor/', views.career_mentor, name='career_mentor'),  # Career mentor
    path('technical_mentor/', views.technical_mentor, name='technical_mentor'),  # Technical mentor
    path('life_mentor/', views.life_mentor, name='life_mentor'),  # Life mentor
    path('leadership_mentor/', views.leadership_mentor, name='leadership_mentor'),  # Leadership mentor
    path('entrepreneurship_mentor/', views.entrepreneurship_mentor, name='entrepreneurship_mentor'),  # Entrepreneurship mentor
    path('financial_mentor/', views.financial_mentor, name='financial_mentor'),  # Financial mentor
    path('health_mentor/', views.health_mentor, name='health_mentor'),  # Health mentor
    path('fitness_mentor/', views.fitness_mentor, name='fitness_mentor'),  # Fitness mentor
    path('nutrition_mentor/', views.nutrition_mentor, name='nutrition_mentor'),  # Nutrition mentor
    path('public_speaking_mentor/', views.public_speaking_mentor, name='public_speaking_mentor'),  # Public speaking mentor
    path('writing_mentor/', views.writing_mentor, name='writing_mentor'),  # Writing mentor
    path('language_mentor/', views.language_mentor, name='language_mentor'),  # Language mentor
    path('design_mentor/', views.design_mentor, name='design_mentor'),  # Design mentor
    path('marketing_mentor/', views.marketing_mentor, name='marketing_mentor'),  # Marketing mentor

    path('about/', views.about, name='about'),  # About Us page
    path('become_mentor/', views.become_mentor, name='become_mentor'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
