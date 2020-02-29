from rest_framework import serializers
from rest.models import User,Hospital,Volunteer

class HospitalSerializer(serializers.ModelSerializer):
  class Meta:
    model = Hospital
    fields = ['name', 'address']


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['name', 'email', 'dob', 'address', 'blood_group', 'password']
    
class VolunteerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Volunteer
    exclude = []


    