from django.contrib import admin
from .models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['emp_name', 'profile', 'salary', 'email','picture', 'media']

admin.site.register(Employee, EmployeeAdmin)