from django.contrib.auth.models import User
from django.db import models



class Group(models.Model):

    groupName = models.ImageField()
    groumImage = models.ImageField()
    groupAdmin = models.ManyToManyField(User)

class Messeges(models.Model):

    messegeBody = models.TextField()
    messegeAutor = models.ForeignKey(User,
                                     on_delete= models.CASCADE)
    messegeGroupId = models.ForeignKey(Group, on_delete=models.CASCADE )
    messegeDate = models.DateTimeField()
    messegeReaded = models.BooleanField()
    messegeReadedTime = models.DateTimeField()

    class Meta:
        ordering = ('-messegeDate',)

    def __str__(self):
        return self.messegeBody




