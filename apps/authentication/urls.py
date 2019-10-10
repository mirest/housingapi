from django.urls import path

from .views import LoginAPIView, RegistrationAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('register/', RegistrationAPIView.as_view()),
]
