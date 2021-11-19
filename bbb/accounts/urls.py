from django.urls import path , include
from . import views
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
from .views import validate_jwt_token #추가
from .views import current_user


urlpatterns =[
    path("signup/", views.SignupView.as_view(), name="signup"),
    path('login/', obtain_jwt_token),
    path('verify/', verify_jwt_token),
    path('refresh/', refresh_jwt_token),
    path('current/', current_user),
    path('validate/', validate_jwt_token),



]