from django.contrib import admin
from busenquiry.models import *

# Register your models here.

admin.site.register(TransportCompany)
admin.site.register(Bus)
admin.site.register(Stops)
admin.site.register(Routes)
admin.site.register(Schedule)
