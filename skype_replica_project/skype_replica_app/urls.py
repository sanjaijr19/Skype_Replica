from django.urls import path
from .views import ProfileViewSet
from . import views
from rest_framework import routers
router =routers.DefaultRouter()

urlpatterns = [
    path('create/', views.ProfileViewSet.as_view(actions={'post': 'create','get':'list'})),
    path('create/<id>/', views.ProfileViewSet.as_view(actions={'post': 'create','get':'retrieve','put':'update','delete':'destroy'})),
]+router.urls