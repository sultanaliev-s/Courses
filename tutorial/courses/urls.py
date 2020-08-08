from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from courses import views

urlpatterns = [
    path('courses/', views.CourseList.as_view(), name = 'coursesList'),
    path('courses/<int:pk>/', views.CourseDetail.as_view(), name = 'courseDetail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)