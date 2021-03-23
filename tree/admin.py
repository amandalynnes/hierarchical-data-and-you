from django.contrib import admin
from tree.models import File
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

admin.site.register(File, DraggableMPTTAdmin)