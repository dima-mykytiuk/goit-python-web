from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-income/', views.add_income, name='add_income'),
    path('add-outcome/', views.add_outcome, name='add_outcome'),
    path('add-category/', views.add_category, name='add_category'),
    path('show-detail/', views.show_detail, name='show_detail'),
]