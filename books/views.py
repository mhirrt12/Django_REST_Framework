from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
class BookList(APIView):

    def get(self, request):

        books = Book.objects.all()

        serializer = BookSerializer(
            books,
            many=True
        )

        return Response(serializer.data)