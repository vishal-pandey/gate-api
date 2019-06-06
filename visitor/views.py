from django.shortcuts import render
from rest_framework import generics, permissions, serializers
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from .serializers import VisitorSerializer
from .models import Visitor
from django.db.models.query import QuerySet
from oauth2_provider.models import get_access_token_model
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from itertools import chain
import collections
# Create your views here.


class VisitorList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer

class VisitorDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer


def index(request):
	return render(request, 'index.html');