'''
Created on Jan 18, 2012

@author: arif
'''
import os
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

MULTIAUTH_DISABLE_GOOGLE_AUTHENTICATOR = getattr(settings, 'MULTIAUTH_DISABLE_GOOGLE_AUTHENTICATOR', False)

MULTIAUTH_TWITTER = getattr(settings, 'MULTIAUTH_TWITTER', False)
MULTIAUTH_LINKEDIN = getattr(settings, 'MULTIAUTH_LINKEDIN', False)
MULTIAUTH_YAHOO = getattr(settings, 'MULTIAUTH_YAHOO', False)
MULTIAUTH_FACEBOOK = getattr(settings, 'MULTIAUTH_FACEBOOK', False)
MULTIAUTH_GOOGLE = getattr(settings, 'MULTIAUTH_GOOGLE', False)
