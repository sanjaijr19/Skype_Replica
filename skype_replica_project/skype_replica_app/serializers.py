from .models import Profile
from rest_framework_mongoengine.serializers import DocumentSerializer

class Profileserializer(DocumentSerializer):
    class Meta:
        model = Profile
        fields = ('id','username','first_name', 'last_name','dob', 'email', 'phone_no', 'location','profile_picture')

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)
