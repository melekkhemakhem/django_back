from rest_framework.serializers import ModelSerializer
from .models import Book,Upload,Student
# data = {
#     "name" :"Django",
#     "description":"Django Rest framework",
#     "created_at":"time"
# }


# serializer for the book
class BookSerializer(ModelSerializer):
    class Meta:
        model=Book
        fields = ["id","name","description","created_at"]
class ImageSerializer(ModelSerializer):
    class Meta:
        model = Upload
        fields = ['url', 'text', 'date']
class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'