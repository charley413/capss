import re
from rest_framework import serializers
from .models import Review
from django.contrib.auth import get_user_model

class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username"]


class ReviewSerializer(serializers.ModelSerializer):
    name=NameSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'




