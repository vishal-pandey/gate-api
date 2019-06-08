from django.urls import path
from visitor import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('visitor/', views.VisitorList.as_view()),
    path('visitor-detail/<pk>/', views.VisitorDetails.as_view()),
    path('visitor-by-number-plate/', views.VisitorByNumberPlate.as_view()),
    path('visitor-by-visit-date/', views.VisitorByVisitDate.as_view()),


    path('', views.index, name='index'),
]