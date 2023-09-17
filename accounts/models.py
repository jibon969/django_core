from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin, AbstractUser
)
from django.conf import settings

DEFAULT_ACTIVATION_DAYS = getattr(settings, 'DEFAULT_ACTIVATION_DAYS', 7)


class UserManager(BaseUserManager):
    def create_user(
            self, email, password=None,
            first_name=None,
            last_name=None,
            date_of_birth=None,
            gender=None,
            contact_number=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            gender=gender,
            contact_number=contact_number
        )
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_staff_user(
            self, email,
            password,
            first_name,
            last_name,
            date_of_birth,
            gender,
            contact_number
    ):
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            gender=gender,
            contact_number=contact_number
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name, last_name, date_of_birth, gender, contact_number):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            gender=gender,
            contact_number=contact_number
        )
        user.is_staff = True
        user.is_admin = True
        # First time login
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='Email Address', max_length=255, unique=True, )
    GENDER = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    date_of_birth = models.DateField(auto_now_add=False)
    contact_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices=GENDER)
    # notice the absence of a "Password field", that's built in.
    USERNAME_FIELD = 'email'
    # Email & Password are required by default.
    REQUIRED_FIELDS = ['first_name', 'last_name', 'dob', 'gender', 'contact_number']

    objects = UserManager()

    def __str__(self):
        return self.email
