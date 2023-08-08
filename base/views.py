from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes

from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .serializers import UserSerializer, UserSerializerWithToken,ScoreSerializer,AverageValueSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


from django.contrib.auth.hashers import make_password
from rest_framework import status


from base.models import Score, AverageValue
import random

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def registerUser(request):
    data = request.data
    try:
        user = User.objects.create(
                first_name = data['first_name'],
                last_name = data['last_name'],
                username = data['email'],
                email = data['email'],
                password = make_password(data['password'])
            )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail':'User with this email already exists'}
        return Response(message, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def getAllScore(request):
    score = Score.objects.all()
    serializer = ScoreSerializer(score, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addScore(request):
    user = request.user
    data = request.data
    score = Score.objects.create(
        user=user,
        name = data['email'],
        score=data['score']
    )
    serializer = ScoreSerializer(score, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getAverageValue(request,pk):
    user = request.user
    averageValue = AverageValue.objects.get(_id=pk)
    serializer = AverageValueSerializer(averageValue, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def setAverageValue(request,value):
    user = request.user
    averageValue = AverageValue.objects.get(_id=1)
    averageValue.averageValue = value    
    averageValue.save()
    serializer = AverageValueSerializer(averageValue, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getWinningValue(request):
    averageValue = AverageValue.objects.get(_id=1)
    serializer = AverageValueSerializer(averageValue, many=False)
    average = serializer.data['averageValue']
    av = average / 5
    num1 = 20 - av
    thislist = []
    i = 0
    k=0
    for k in range(500):
        while i < num1:
            j = i % av +1
            thislist.append(j) 
            i += 1
        i = 0
        j = 1
        while i < av:
            if num1 == 0:
                j=20
            else:
                j = i % (num1+1) + av +1
            thislist.append(j) 
            i += 1
    
    selNum = random.randrange(490*10)
    return Response(thislist[selNum]*5)
