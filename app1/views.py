from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import *
from .serializers import *

# Create your views here.

class Feedback_details(APIView):
    def get(self, request, format=None):
        snippets = Feedback.objects.all()
        serializer = FeedbackSerializers(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
      serializer = FeedbackSerializers(data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class Feedback_Change(APIView):
#     def get_object(self, pk):
#         try:
#             return Feedback.objects.get(pk=pk)
#         except Feedback.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = FeedbackSerializers(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = FeedbackSerializers(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):
    #   snippet = self.get_object(pk)
    #   snippet.delete()
    #   return Response(status=status.HTTP_204_NO_CONTENT)
