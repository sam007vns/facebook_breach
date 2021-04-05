from django.contrib import admin
from .models import *



@admin.register(facebook_data)
class facebook_dataAdmin(admin.ModelAdmin):
	list_display = ('mobile_no','registration','info',)
	search_fields = ('mobile_no','registration','info__icontains',)

@admin.register(user_matched)
class user_matchedAdmin(admin.ModelAdmin):
	list_display = ('mobile_no','info','registration','date_added',)
	search_fields = ('date_added','mobile_no',)
@admin.register(user_not_matched)
class user_not_matchedAdmin(admin.ModelAdmin):
	list_display = ('phone','date_added',)
	search_fields = ('date_added','phone',)
