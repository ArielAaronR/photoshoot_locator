from django.db import models
from django.contrib import messages
from django.contrib.messages import get_messages
import re
# Create your models here.
class UserManager(models.Manager):
    def basic_validation(self, request):
        if request.POST["password"] != request.POST["password_confirm"]:
            messages.error(request, "Password must match confirm password")

        if len(request.POST["first_name"]) < 2:
            messages.error(request, "First Name must be at least 2 characters")

        if len(request.POST["last_name"]) < 2:
            messages.error(request, "First Name must be at least 2 characters")
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(request.POST['email']):
            messages.error(request, "Invalid email address!")
        storage = messages.get_messages(request)
        storage.used = False
        return len(storage) == 0


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=320)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Marker(models.Model):
    name = models.CharField(max_length=255)
    address= models.CharField(max_length=255)
    image = models.ImageField(upload_to=None)
    descriptors = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<Marker object: id: {self.id}, photo: {self.image}, title: {self.name}, desc: {self.description}, address: {self.address}>"


