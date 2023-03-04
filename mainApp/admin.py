from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdmin
from django.contrib.auth.models import User
from .models import *
# Register your models here.

# class DoctorInline(admin.StackedInline):
#     model = Doctor
#     can_delete = True
#     verbose_name_plural = 'doctor'

# class UserAdmin(BaseUserAdmin):
#     inlines = (DoctorInline,)

# admin.site.unregister(User)
# admin.site.register(User, BaseUserAdmin)

admin.site.register(Patient)
admin.site.register(Room)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Admission)
admin.site.register(Test)
admin.site.register(Operation)
