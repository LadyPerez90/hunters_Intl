from django.db import models
import re

class UserManager(models.Manager):
    def reg_validator(self, postData):
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors = {}

        if len(postData['first_name']) < 2:
            errors['first_name'] = "First Name must be at least 2 characters"

        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last Name must be at least 2 characters"

        if not email_regex.match(postData['email']):
            errors['email'] = "Invalid email Format"

        emailCheck = self.filter(email=postData['email'])
        if emailCheck:
            errors['email'] = "Email already in use"

        if len(postData['password']) < 5:
            errors['password'] = "Password should be at least 5 characters"

        if postData['password'] != postData['confirm_password']:
            errors['password'] = "Passwords do not match"
        return errors


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_pw = models.CharField(max_length=255)
    objects = UserManager()

# class Document(models.Model):
#     docfile = models.FileField(upload_to='Documents/VS/Assignments/back_coing/python_stack/django/hunters_Intl/hunter_app/static/image/%Y/%m/%d')
#     user = models.ForeignKey(User, related_name='files', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

class User_Post(models.Model):
    message = models.CharField(max_length=500)
    poster = models.ForeignKey(User, related_name='user_posts', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='liked_posts')

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    user_post = models.ForeignKey(User_Post, related_name="post_comments", on_delete=models.CASCADE)