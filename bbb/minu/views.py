from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .serializers import ReviewSerializer
from .models import Review
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from django.db.models import Q

class ReviewViewSet(ModelViewSet):
    queryset=Review.objects.all()
    serializer_class = ReviewSerializer
    #permission_classes = [AllowAny]

    def get_queryset(self):
        qs=super().get_queryset()
        qs=qs.filter(
            Q(name=self.request.user)
        )
        return qs

