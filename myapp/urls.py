from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('Achievements.html', views.Achievements, name='Achievements'),
    path('contact.html', views.contact, name='contact'),
    path('gallery.html', views.gallery, name='gallery'),
    path('kiloflight.html', views.kiloflight, name = 'kiloflight'),
    path('outreach.html', views.outreach, name = 'outreach'),
    path('project.html', views.project, name = 'project'),
    path('team.html/', views.team, name='team')
]