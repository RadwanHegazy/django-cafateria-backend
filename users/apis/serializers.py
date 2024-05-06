from rest_framework import serializers
from ..models import User
from rest_framework.validators import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterSerializer (serializers.ModelSerializer) : 
    class Meta : 
        model = User
        fields = ("id",'full_name','email','password','picture')
    
    def save(self, **kwargs):
        self.user = User.objects.create_user(**self.validated_data)
        return self.user
    
    @property
    def tokens (self): 
        token = RefreshToken.for_user(self.user)
        return {
            'token' : str(token.access_token)
        }

class LoginSerializer (serializers.Serializer) : 
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs['email']
        password = attrs['password']

        try : 
            self.user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise ValidationError({
                'message' : 'invalid email'
            },code=400)
        
        if not self.user.check_password(password) : 
            raise ValidationError({
                'message' : 'invalid password'
            },code=400)
        
        return attrs
    
    @property
    def tokens (self): 
        token = RefreshToken.for_user(self.user)
        return {
            'token' : str(token.access_token)
        }