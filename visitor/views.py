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

class VisitorByNumberPlate(APIView):
	permission_classes = [permissions.IsAuthenticated]
	def get(self, request, format=None):
		return Response(request.data)

	def post(self, request, format=None):

		if request.data['all']=='1':
			queryset = Visitor.objects.filter(Q(number_plate__iexact=request.data['number_plate'])).values_list('id','visit_date','card_number','name','address','mobile','number_plate','destination','purpose','intime','outtime').distinct()[:]
		else:
			queryset = Visitor.objects.filter(Q(number_plate__iexact=request.data['number_plate'])).values_list('id','visit_date','card_number','name','address','mobile','number_plate','destination','purpose','intime','outtime').distinct()[:1]

		return Response(queryset)

class VisitorByVisitDate(APIView):
	permission_classes = [permissions.IsAuthenticated]
	def get(self, request, format=None):
		return Response(request.data)

	def post(self, request, format=None):
		queryset = Visitor.objects.filter(Q(visit_date__iexact=request.data['visit_date'])).values_list('id','visit_date','card_number','name','address','mobile','number_plate','destination','purpose','intime','outtime').distinct()[:]
		return Response(queryset)	



def index(request):
	return render(request, 'index.html');