import imp
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response as DjangoRestResponse
from rest_framework import status
from home.models.users import Users
from home.serializers.users_serializers import UsersSerializer
# Create your views here.

@api_view(['GET'])
def get_user(request):
    user_obj=Users.objects.all()
    serializer =UsersSerializer(user_obj,many=True)
    return DjangoRestResponse(
         {
            "User Data": serializer.data,
        },
        status=status.HTTP_201_CREATED,
    )

@api_view(['POST'])
def post_user(request):
    user_data=request.data
    serializer =UsersSerializer(data=user_data)
    if not serializer.is_valid():
        print(serializer.errors)
        return DjangoRestResponse({"msg": "something went wrong",},status=status.HTTP_400_BAD_REQUEST)   
    
    serializer.save()
    
    return DjangoRestResponse({"payload": serializer.data,},status=status.HTTP_201_CREATED)