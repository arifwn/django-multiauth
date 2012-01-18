'''
Created on Jan 4, 2012

@author: arif
'''
from django.contrib import admin
from multiauth.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'multifactor_auth_enabled']

admin.site.register(Profile, ProfileAdmin)
