
from rest_framework import serializers
from .models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model =Book
        fields = ['title', 'description', 'created_at']