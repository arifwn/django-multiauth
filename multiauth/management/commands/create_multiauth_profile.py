# coding: utf-8

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from multiauth.models import Profile

class Command(BaseCommand):
    help = "Create multiauth profile if not exist for a user."
    
    def handle(self, *args, **options):
        count = 0
        print 'creating user profile...'
        for user in User.objects.all():
            try:
                user.multiauth_profile
            except:
                Profile.objects.create(user=user)
                print 'profile created for user', user.username
                count += 1
        
        print count, 'profile created'
