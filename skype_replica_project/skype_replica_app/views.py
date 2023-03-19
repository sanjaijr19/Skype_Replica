
from django.shortcuts import render
from .models import Profile
from rest_framework import viewsets,generics
from .serializers import Profileserializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = Profileserializer
    lookup_field = 'id'


