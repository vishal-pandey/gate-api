from rest_framework import serializers
from .models import Visitor
from rest_framework import generics, permissions, serializers
from django.contrib.auth import get_user_model
from oauth2_provider.models import AbstractAccessToken

class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = ("visit_date","card_number","name","address","mobile","number_plate","destination","purpose","intime","outtime")