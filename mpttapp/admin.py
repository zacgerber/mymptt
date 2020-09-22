from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from mpttapp.models import Mydata

# Register your models here.
admin.site.register(Mydata, DraggableMPTTAdmin)
