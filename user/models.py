from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):

    def _create_user(self,username,password, **kwargs):
        user = self.model(
            username=username,
            **kwargs
        )
        user.set_password(password)
        user.save()
    
    def create_user(self,username, password, **kwargs):
        self._create_user(username,password, **kwargs)
 

    def create_superuser(self, username, password, **kwargs):
        kwargs.setdefault('is_superuser', True)
        self._create_user(username,password, **kwargs)



class User(AbstractBaseUser, PermissionsMixin):
    
    USERNAME_FIELD = 'username'

    username = models.CharField(
        unique=True,
        max_length=20,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now = True,
    )

    objects = UserManager()

    @property
    def is_staff(self):
        return self.is_superuser