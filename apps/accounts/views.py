from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from rest_framework import permissions
from apps.accounts.models import User
from common.permissions import UserIsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.accounts.serializers import UserNewsSerializer
from rest_framework import status
from apps.accounts.serializers import CreateUserSerializer, UpdateUserSerailizer
# Create your views here.


@api_view(['GET'])
def user_newses(request, *args, **kwargs):
    user = get_object_or_404(User,pk=kwargs.get('pk'))
    serializer = UserNewsSerializer(user)
    return Response(serializer.data,status=status.HTTP_200_OK)

    




class CreateUserView(generics.CreateAPIView):
    serializer_class =CreateUserSerializer
    permission_classes = (permissions.AllowAny,)



class UpdateUserView(generics.UpdateAPIView):
    serializer_class= UpdateUserSerailizer
    permission_classes= (permissions.IsAuthenticated,UserIsOwnerOrReadOnly)
    queryset= User.objects.all()


