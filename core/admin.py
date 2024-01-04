from django.contrib import admin

# Register your models here.

from core.models import About, Client, RecentWork,Service, Blog,BlogCategory,Education, Experience, Skill, Project,ProjectCategory

admin.site.register(About)
admin.site.register(Client)
admin.site.register(RecentWork)
admin.site.register(Service)
admin.site.register(Blog)
admin.site.register(BlogCategory)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(ProjectCategory)
 

