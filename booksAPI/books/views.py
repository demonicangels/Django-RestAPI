#file containing all endpoints of the API
from django.http import JsonResponse
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


@api_view(['GET', 'POST']) #decorator that takes a list of allowed type of methods
def bookList (request):
    
    if request.method == 'GET': 
        #get all books
        books = Book.objects.all()
        #serialize them
        serialized_books = BookSerializer(books, many=True)
        #return JSON response
        #if you want it serialized not as a list but an obj you you need to put serialized_books.data in a dictionary so ({"books": serialized_books.data})
        return JsonResponse({"books": serialized_books.data}) 
    elif request.method == 'POST':
        newBook = BookSerializer(data=request.data)
        if newBook.is_valid():
            newBook.save()
            return Response(newBook.data, status=status.HTTP_201_CREATED)
        else:
            return Response(newBook.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'detail': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET', 'PUT', 'DELETE'])
def bookDetail(request,id):
    try:
        
        book = Book.objects.get(id=id)
            
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serialized_book = BookSerializer(book)
        return Response(serialized_book.data)
            
    elif request.method == 'PUT':
        serialized_book = BookSerializer(book, data=request.data)
        if (serialized_book.is_valid()):
            serialized_book.save()
            return Response(serialized_book.data)
        else:
            return Response(serialized_book.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        book = Book.objects.get(id=id)
        if(book is not None):
            book.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    