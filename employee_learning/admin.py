from django.contrib import admin
from .models import Employee,Division,PersonalInfo,LearningCourse

admin.site.register(Employee)
admin.site.register(Division)
admin.site.register(PersonalInfo)
admin.site.register(LearningCourse)