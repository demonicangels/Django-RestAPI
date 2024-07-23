#class serializing the python obj to json obj
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    # meta data class of the serializer 
    class Meta:
        model = Book
        fields = ['id','title', 'author']
        