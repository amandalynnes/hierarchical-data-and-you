from django.contrib import admin
from tree.models import Folder
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

admin.site.register(Folder, DraggableMPTTAdmin)
