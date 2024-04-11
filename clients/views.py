from django.shortcuts import render

# Create your views here.

# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import ClientSerializer
from .models import Client

# create a viewset


class ClientsViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = Client.objects.all()

	# specify serializer to be used
	serializer_class = ClientSerializer
