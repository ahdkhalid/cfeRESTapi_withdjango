from django.contrib import admin

from .forms import StatusForm
from .models import Status as StatusModel

class StatusAdmin(admin.ModelAdmin):
    list_display = ['user','__str__','image']
    form = StatusForm
    # class Meta:
    #     model =StatusModel
admin.site.register(StatusModel,StatusAdmin)