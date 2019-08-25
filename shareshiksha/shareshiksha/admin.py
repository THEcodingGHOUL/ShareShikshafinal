from django.contrib import admin

# Register your models here.
# Register the models by copying the following text into the bottom of the file. This code simply imports the models and then calls admin.site.register to register each of them.

from .models import Admin,Community,CommunitySchoolRel,School,Teacher,Volunteer,Grievance

admin.site.register(Admin)
admin.site.register(Community)
admin.site.register(CommunitySchoolRel)
admin.site.register(School)
admin.site.register(Teacher)
admin.site.register(Volunteer)
admin.site.register(Grievance)