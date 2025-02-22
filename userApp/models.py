from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password=None,phone_number=None,**kwargs):
        if not  email or phone_number:
            raise ValueError("Email or phone number is must")
        email = self.normalize_email(email)
        user = self.model(email=email,phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)

        return user
    

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15,unique=True)
    full_name = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']
    def __str__(self):
        return self.email
    

class PatientProfile(models.Model):
    GENDER_CHOICES = (
        ('M','Mail'),('F','Femail')
    )
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=1)

    def __str__(self):
        return self.user.email