from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import player
from .serializer import playerserializer

@api_view(["GET"])
def listview(request):
	listis = player.objects.all()
	serializer = playerserializer(listis,many=True)
	return Response(serializer.data)
