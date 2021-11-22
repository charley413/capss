from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('input', views.ReviewViewSet)


urlpatterns =[
      path('minutes/', include(router.urls)),


]

