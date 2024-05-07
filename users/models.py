from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser


class Managers (BaseUserManager) : 
    def create_user (self,password,**fields) : 
        user = self.model(**fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser (self,**fields) :
        fields['is_staff'] = True 
        fields['is_superuser'] = True 
        return self.create_user(**fields)


class User (AbstractUser) : 
    objects = Managers()

    username = None
    user_permissions = None
    groups = None
    first_name = None
    last_name = None

    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=225)
    picture = models.ImageField(upload_to='user-pics/',default='user.png')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('full_name',)

    cafateria = models.ForeignKey('cafateria.Cafateria',related_name='user_cafateria',null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.full_name