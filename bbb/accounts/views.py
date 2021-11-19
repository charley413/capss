from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import permissions, status, generics
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from .serializers import SignupSerializer, UserSerializerWithToken, UserSerializer
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer #추가
from rest_framework.response import Response    #추가
from rest_framework.decorators import api_view   #추가
from rest_framework.views import APIView






class SignupView(CreateAPIView):
    model = get_user_model()
    serializer_class = SignupSerializer
    permission_classes = [
        AllowAny,
    ]

@api_view(['GET']) #추가
def validate_jwt_token(request):

    try:
        token = request.META['HTTP_AUTHORIZATION']
        data = {'token': token.split()[1]}
        valid_data = VerifyJSONWebTokenSerializer().validate(data)
    except Exception as e:
        return Response(e)

    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def current_user(request):

    serializer = UserSerializer(request.user)
    return Response(serializer.data)



class UserList(APIView):

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



