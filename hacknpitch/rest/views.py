from django.shortcuts import render
from django.http import Http404

from rest.models import User, Hospital, Volunteer
from rest.serializers import UserSerializer, HospitalSerializer, VolunteerSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

# Create your views here.
class HospitalList(generics.ListAPIView):
  serializer_class = HospitalSerializer
  queryset = Hospital.objects.all()
  
class LoginView(APIView):
  """
  User login view.
  Only supports POST.
  """
  def post(self, request, format=None):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
      user = User.objects.get(email=serializer.data['email'])
      if user.password == serializer.data['password']:
        return Response({status: True}, status=status.HTTP_202_ACCEPTED)
      return Response({status: False}, status=status)
    return Response({status: False}, status=status.HTTP_400_BAD_REQUEST)