from .models import Profile
from rest_framework_mongoengine.serializers import DocumentSerializer

class Profileserializer(DocumentSerializer):
    class Meta:
        model = Profile
        fields = ('id','username','first_name', 'last_name','dob','gender', 'email', 'phone_no','city', 'state','country','profile_picture','user_active')

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)
