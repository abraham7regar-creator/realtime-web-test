from django.urls import path

from . import views

urlpatterns = [
    path('', views.AppList.as_view()),
    path('<int:pk>/', views.AppDetail.as_view()), 
    # api/v1/app/1
]