from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from DimosoApp.models import *

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ["name", "post_date"]
	#prepopulated_fields={'slug':('name',)}

admin.site.register(Post, PostAdmin)
admin.site.register(MyProject)
admin.site.register(Expertise)
admin.site.register(Experience)
admin.site.register(Skills)
admin.site.register(Summary)
admin.site.register(Contact)