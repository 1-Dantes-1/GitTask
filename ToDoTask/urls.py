from django.urls import path
from . import views

urlpatterns = [
    path('taskApiView/', views.TaskAPIView.as_view()),
    path('tagApiView/', views.TagAPIView.as_view())
]
