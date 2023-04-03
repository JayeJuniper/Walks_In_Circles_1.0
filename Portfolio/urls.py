from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('Gallery/', views.gallery, name='gallery'),
    path('Gallery/Upload/', views.photo_upload, name='photo_upload'),
    path('Gallery/<int:pk>/edit/', views.photo_edit, name='photo_edit'),
    path('Gallery/<int:pk>/delete/', views.photo_delete, name='photo_delete'),
    path('Expeditions/', views.expedition_list, name='expeditions'),
    path('Expeditions/New/', views.expedition_new, name='expedition_new'),
    path('Expeditions/<int:pk>/', views.expedition_detail, name='expedition_detail'),
    path('Expeditions/<int:pk>/edit/', views.expedition_edit, name='expedition_edit'),
    path('Expeditions/<int:pk>/delete/', views.expedition_delete, name='expedition_delete'),
    path('Jeep/', views.jeep, name='jeep'),
    path('Jeep/New/', views.jeep_new, name='jeep_new'),
    path('Jeep/<int:pk>/', views.jeep_detail, name='jeep_detail'),
    path('Jeep/<int:pk>/edit/', views.jeep_edit, name='jeep_edit'),
    path('Jeep/<int:pk>/delete/', views.jeep_delete, name='jeep_delete'),
    path('Articles/', views.article_list, name='article_list'),
    path('Article/<int:pk>/', views.article_detail, name='article_detail'),
    path('Article/New/', views.article_new, name='article_new'),
    path('Article/<int:pk>/edit/', views.article_edit, name='article_edit'),
    path('Article/<int:pk>/delete/', views.article_delete, name='article_delete'),
    path('Portfolio/New/', views.portfolio_new, name='portfolio_new'),
    path('Portfolio/<int:pk>/', views.portfolio_detail, name='portfolio_detail'),
    path('Portfolio/<int:pk>/edit', views.portfolio_edit, name='portfolio_edit'),
]
