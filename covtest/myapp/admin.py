from django.contrib import admin

# Register your models here.
from .models import Order, Lab

admin.site.register(Order)
admin.site.register(Lab)