from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
     class Meta:
         model = User
         fields = ['id', 'email', 'phone', "first_name", 'last_name']
         
class UserCreateSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    phone = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email exists try a new one")
        return value
    
    def validate_phone(self, value):
        if User.objects.filter(phone=value).exists():
            raise serializers.ValidationError("This phone exists try a new one")
        return value
    
    def create(self, validated_data):
        email = validated_data.get('email')
        phone = validated_data.get('phone')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        
        user = User.objects.create(
            email=email,
            phone=phone,
            first_name=first_name,
            last_name=last_name,
        )
        
        return user