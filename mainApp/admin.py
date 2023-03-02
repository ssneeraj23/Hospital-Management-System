from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Patient)
admin.site.register(Room)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Admission)
admin.site.register(Test)
admin.site.register(Operation)