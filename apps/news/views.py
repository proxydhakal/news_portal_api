from django.shortcuts import render
from rest_framework import generics
from rest_framework import authentication
from rest_framework import permissions
from rest_framework_simplejwt import authentication
from apps.news import serializers
from apps.news.models import News
from common.permissions import IsAdminOrJournalist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


@api_view(['GET'])
def news_categories(request,*args,**kwargs):
    categories=dict(News.CHOICES)
    return Response(categories,status=status.HTTP_200_OK)




class CreateNewsAPIView(generics.CreateAPIView):
    authentication_classes =[authentication.JWTAuthentication,]
    permission_classes =[IsAdminOrJournalist]
    serializer_class = serializers.NewsSerializer
    





class UpdateNewsAPIView(generics.UpdateAPIView):
    authentication_classes =[authentication.JWTAuthentication,]
    permission_classes =[IsAdminOrJournalist]
    serializer_class = serializers.NewsSerializer
    queryset = News.objects.all()
    



class ListNewsAPIView(generics.ListAPIView):
    serializer_class = serializers.NewsSerializer
    queryset = News.objects.all()
    permission_classes = [permissions.AllowAny]
    


class SingleNewsAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.NewsSerializer
    queryset = News.objects.all()
    permission_classes = [permissions.AllowAny]
    


class DeleteNewsAPIView(generics.DestroyAPIView):
    queryset = News.objects.all()
    permission_classes =[IsAdminOrJournalist]
    



class CommentCreateAPIView(generics.CreateAPIView):
    authentication_classes =[authentication.JWTAuthentication,]
    serializer_class = serializers.NewsSerializer
    
