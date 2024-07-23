from django.contrib import admin
from .models import Book

#registering our model to the admin webpage in our app 
# not mandatory if we prefer not to use the admin webpage
admin.site.register(Book)
