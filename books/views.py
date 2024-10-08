from venv import logger
from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView,UpdateAPIView, DestroyAPIView
from .models import Book,Student
from .serializer import BookSerializer,ImageSerializer
from rest_framework import response,status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Upload
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .serializer import StudentSerializer
# Create your views here.
class ListBooksAPIView(ListAPIView):
   queryset= Book.objects.all()
   serializer_class = BookSerializer
class RetrieveBookAPIView(RetrieveAPIView):
   queryset = Book.objects.all()
   serializer_class = BookSerializer
   #lookup_field= 'pk'
   def get(self, request, *args, **kwargs):
      id=kwargs.get("id","")
      try:
        #Retrieving a book from the database
        book = Book.objects.get(id=id)

        #serialization process
        serializer = BookSerializer(book)
      except Book.DoesNotExist:
         return response.Response({"message": "this Book is not found! "}, status=status.HTTP_404_NOT_FOUND)
      except Exception:
         return response.Response({"message": "server Eror! "}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      
      return response.Response(serializer.data, status=status.HTTP_200_OK)
class RegisterBookAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DeleteBookAPIView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UpdateBookAPIView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class ListBooksAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class RetrieveBookAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'  # Utilisation de 'id' comme champ de recherche

class RegisterBookAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UpdateBookAPIView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'  # Utilisation de 'id' comme champ de recherche

class DeleteBookAPIView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'  # Utilisation de 'id' comme champ de recherche
class Upload_view(CreateAPIView):
    queryset = Upload.objects.all()
    serializer_class = ImageSerializer
class Upload_view(CreateAPIView):
    queryset = Upload.objects.all()
    serializer_class = ImageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Enregistrer l'objet dans la base de données
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# # class ListImagesAPIView(ListAPIView):
# #     queryset = Upload.objects.all()
# #     serializer_class = ImageSerializer
class ListImagesAPIView(ListAPIView):
    queryset = Upload.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [AllowAny]  
# # class Upload_view(CreateAPIView):
# #     def post(self, request):
# #         serializer = ImageSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def studentApi(request, id=0):
    if request.method == 'GET':
        students = Upload.objects.all()
        student_serializer = ImageSerializer(students, many=True)
        return JsonResponse(student_serializer.data, safe=False)

    elif request.method == 'POST':
        data = request.POST
        file = request.FILES.get('url')

        logger.info(f"Received data: {data}")
        logger.info(f"Received file: {file}")

        upload_data = {
            'text': data['text'],
            'url': file,
        }
        student_serializer = ImageSerializer(data=upload_data)

        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        logger.error("Failed to validate student data.")
        return JsonResponse("Failed to Add", safe=False)

    elif request.method == 'PUT':
        student_data = JSONParser().parse(request)
        student = Upload.objects.get(id=id)
        student_serializer = ImageSerializer(student, data=student_data)

        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", status=400)

    elif request.method == 'DELETE':
        if id == 0:
            # If no ID is specified, delete all records
            Upload.objects.all().delete()
            return JsonResponse("All Records Deleted Successfully", safe=False)
        else:
            # If an ID is specified, delete only that record
            try:
                student = Upload.objects.get(id=id)
                student.delete()
                return JsonResponse("Deleted Successfully", safe=False)
            except Upload.DoesNotExist:
                return JsonResponse("Record Not Found", status=404)