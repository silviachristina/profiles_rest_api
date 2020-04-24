from django.db import models
# Is the base of the django standard User Model (we're gonna build on top of it)
from django.contrib.auth.models import AbstractBaseUser
# Alows to add permitions to your users model, what they can or canoot do in your system  
from django.contrib.auth.models import PermissionsMixin
# Teach django how to use our new UserProfile module though a Manager class
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user model."""

    def create_user(self, email, name, password=None):
        """Creates a new user profile object."""

        if not email:
            raise ValueError('Users must have an email address.')

        # lowercase
        email = self.normalize_email(email)
        user  = self.model(email=email, name=name)

        # set the passowrd encrypted (hash)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates and saves a new superuser with given details."""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a "user profile" inside our system."""

    email = models.EmailField(max_length=255, unique=True)
    name  = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Used to get a users full name."""
        return self.name
    
    def get_short_name(self):
        """Used to get a users short name."""
        return self.name
    
    def __str__(self):
        """Django uses this when it needs to convert the object to a string"""
        return self.email
    
    



    # object manager is another class used to manager our user profile 