from django.db import models

# Create your models here. = models.CharField(max_length=250)
#     groupImage
class Messeges(models.Model):

    messegeBody = models.TextField()


class Groups(models.Model):

    groupName = models.ImageField()