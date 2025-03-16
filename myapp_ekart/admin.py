# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Member

# Register your models here.
# admin.site.register(Member)# display all the members in Member table
# below is display the data in list format
class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname","phone", "joined_date",)
  
admin.site.register(Member, MemberAdmin)