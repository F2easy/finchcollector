from django.contrib import admin

# import our cat model
from .models import Finch

# Register your models here.
admin.site.register(Finch)