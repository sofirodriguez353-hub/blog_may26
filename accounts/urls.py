from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('registrar/', SignUpView.as_view(), name='signup'),
]