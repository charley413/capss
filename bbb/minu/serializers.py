import re
from rest_framework import serializers
from .models import Review
from django.contrib.auth import get_user_model

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ["id", "name", "created_at", "content", "summary", "title", "users_in", "date"]

