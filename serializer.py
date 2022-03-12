from rest_framework import serializers
from .models import player

class playerserializer(serializers.ModelSerializer):
	class Meta:
		model = player
		fields = "__all__"