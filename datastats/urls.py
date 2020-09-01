from django.urls import path

from . import views

app_name = 'datastats'
urlpatterns = [
    path('', views.summary, name='summary'),
    path('<int:dataset_id>/', views.dataset, name='dataset'),
]