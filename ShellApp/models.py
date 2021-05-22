from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"<Book:{self.title} ({self.desc})>"

    
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    notes = models.TextField(default="")
    books = models.ManyToManyField("Book", related_name= "authors")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"<Author : {self.first_name}({self.last_name})>"