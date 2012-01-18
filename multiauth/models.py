from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='multiauth_profile')
        
    # Multifactor Auth support
    multifactor_auth_enabled = models.BooleanField(default=False)
    
    # Google Authenticator
    authenticator_key = models.TextField(blank=True)
    
    # Additional details
    avatar = models.ImageField(upload_to='image/avatar/%Y/%m', blank=True, max_length=200)
    
    def __unicode__(self):
        return self.user.username

# -- OAuth 1.0 services --

class TwitterProfile(models.Model):
    # Twitter: https://dev.twitter.com/docs/auth/implementing-sign-twitter
    twitter_user_id = models.CharField(max_length=200, blank=True)
    twitter_oauth_token = models.TextField(blank=True)
    twitter_oauth_secret = models.TextField(blank=True)
    profile = models.OneToOneField(Profile, related_name='twitter')
    avatar = models.ImageField(upload_to='image/twitter_avatar/%Y/%m', blank=True, max_length=200)


class LinkedInProfile(models.Model):
    # LinkedIn: http://developer.linkedin.com/documents/linkedins-oauth-details
    linkedin_user_id = models.CharField(max_length=200, blank=True)
    linkedin_oauth_token = models.TextField(blank=True)
    linkedin_oauth_secret = models.TextField(blank=True)
    profile = models.OneToOneField(Profile, related_name='linkedin')
    avatar = models.ImageField(upload_to='image/linkedin_avatar/%Y/%m', blank=True, max_length=200)


class YahooProfile(models.Model):
    # Yahoo: http://developer.yahoo.com/oauth/guide/index.html
    yahoo_user_id = models.CharField(max_length=200, blank=True)
    yahoo_oauth_token = models.TextField(blank=True)
    yahoo_oauth_secret = models.TextField(blank=True)
    profile = models.OneToOneField(Profile, related_name='yahoo')
    avatar = models.ImageField(upload_to='image/yahoo_avatar/%Y/%m', blank=True, max_length=200)


# -- OAuth 2.0 services --

class FacebookProfile(models.Model):
    # Facebook: https://developers.facebook.com/docs/authentication/
    facebook_user_id = models.CharField(max_length=200, blank=True)
    facebook_access_token = models.TextField(blank=True)
    profile = models.OneToOneField(Profile, related_name='facebook')
    avatar = models.ImageField(upload_to='image/facebook_avatar/%Y/%m', blank=True, max_length=200)
    
class GoogleProfile(models.Model):
    # Google: http://code.google.com/apis/accounts/docs/OAuth2WebServer.html
    google_user_id = models.CharField(max_length=200, blank=True)
    google_access_token = models.TextField(blank=True)
    profile = models.OneToOneField(Profile, related_name='google')
    avatar = models.ImageField(upload_to='image/google_avatar/%Y/%m', blank=True, max_length=200)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
