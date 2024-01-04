from django.contrib import admin

# Register your models here.

from core.models import About, Client, RecentWork,Service

admin.site.register(About)
admin.site.register(Client)
admin.site.register(RecentWork)
admin.site.register(Service)


