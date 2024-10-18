from django.db import models

# Create your models here.
class HappyPlace(models.Model):
    f_name = models.CharField(max_length=50, blank=False, null=False) #field for first name, character length denoted, and value must be inputted by user
    l_name = models.CharField(max_length=50, blank=False, null=False) #field for last name, character length denoted, and value must be inputted by user
    location = models.CharField(max_length=75, blank=False, null=False) #field location for HappyPlace, character length denoted, and value must be inputted by user
    comments =models.TextField(max_length=200, blank=True, null=True) #field for comments by user. Character length restricted but user does not have to input a value
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): #returns string instance of an object
         return "Name: {} {}, Location: {}, Comment: {}".format(self.f_name,self.l_name,self.location,self.comments)#returns first name, last name, location, and a comment (if applicable) by users within the format provided
