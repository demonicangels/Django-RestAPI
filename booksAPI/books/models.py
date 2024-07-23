from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

#special method known as dunder method (or magic method) that serves the purpouse of defining what should be returned when the object is converted to a string presentation (e.g. print())
    def __str__(self):
        return self.title + ' by ' + self.author