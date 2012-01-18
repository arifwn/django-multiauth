'''
Created on Jan 17, 2012

@author: arif
'''
from django.template import Library
register = Library()


from django.template import Library, Node, Variable, VariableDoesNotExist, TemplateSyntaxError
from django.core.files import File

class VersionNode(Node):
    def __init__(self, src, version_prefix):
        self.src = Variable(src)
        if (version_prefix[0] == version_prefix[-1] and version_prefix[0] in ('"', "'")):
            self.version_prefix = version_prefix[1:-1]
        else:
            self.version_prefix = None
            self.version_prefix_var = Variable(version_prefix)
        
    def render(self, context):
        try:
            source = self.src.resolve(context)
        except VariableDoesNotExist:
            return None
        if self.version_prefix:
            version_prefix = self.version_prefix
        else:
            try:
                version_prefix = self.version_prefix_var.resolve(context)
            except VariableDoesNotExist:
                return None
        site = context.get('site', get_default_site())
        directory = site.directory
        try:
            if isinstance(source, FileObject):
                site = source.site
                source = source.path
            if isinstance(source, File):
                source = source.name
            source = force_unicode(source)
            if FORCE_PLACEHOLDER:
                source = PLACEHOLDER
            elif SHOW_PLACEHOLDER and not site.storage.isfile(source):
                source = PLACEHOLDER
            version_path = get_version_path(source, version_prefix, site=site)
            if not site.storage.isfile(version_path):
                version_path = version_generator(source, version_prefix, site=site)
            elif site.storage.modified_time(source) > site.storage.modified_time(version_path):
                version_path = version_generator(source, version_prefix, force=True, site=site)
            return site.storage.url(version_path)
        except:
            return ""

