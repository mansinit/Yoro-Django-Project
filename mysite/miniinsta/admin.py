from django.contrib import admin

# Register your models here.
from .models import Pictures

admin.site.register([Pictures])