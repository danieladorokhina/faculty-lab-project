from django.contrib import admin

from .models import Department, Program, HomePage, Coordinator, Teacher

admin.site.register(Department)
admin.site.register(Program)
admin.site.register(HomePage)
admin.site.register(Coordinator) 
admin.site.register(Teacher)