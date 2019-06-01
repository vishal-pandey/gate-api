from django.urls import path
from visitor import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('visitor/', views.VisitorList.as_view()),
]