from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import BookSerializer
from django.http import JsonResponse
from .models import *
from rest_framework import status



# Create your views here.

# crud operations using get and post

@api_view(['GET', 'POST'])
def Book_list(request):
    if request.method == 'GET':
        print('hello world')
        all_books = Book.objects.all()
        serializer = BookSerializer(all_books, many=True)
        data = {
            "msg": "Data fetched successfully",
            "data": serializer.data
        }
        return JsonResponse(data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'msg': 'Data saved successfully'
            }
            return JsonResponse(data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(["GET", "PUT", "PATCH", "DELETE"])
def Bookdetails(request,pk):
    try:
        book=Book.objects.get(id=pk)
        print('book doesnot exist')
    except :
        data={
            "msg":'book doesnot exist'
        }
        return JsonResponse(data)   

    if request.method == 'GET':
        
            serilizer=BookSerializer(book)
            data={
                "msg":"data is get",
                "data":serilizer.data
            }
            return JsonResponse(data)
       
              


    elif request.method == "PUT":
        print('put method called')
        serilizer=BookSerializer(book,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            data={
                "msg":"data is updated using PUT",
                "data":serilizer.data
            }
            return JsonResponse(data)
        return JsonResponse({"message": "Invalid HTTP method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    elif  request.method=="PATCH":
        serilizer=BookSerializer(book,request.data,partial=True)
        if serilizer.is_valid():
            serilizer.save()
            data={
                "msg":"data is updated using Patch",
                "data":serilizer.data
            }
            return JsonResponse(data)
        return JsonResponse(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)   


    elif request.method == 'DELETE':
        book.delete()
        context={
            "msg":"data has been deleted happy "
        }
        return JsonResponse(context)   
      

