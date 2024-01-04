from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path("", views.home, name='home'),
    path('project-details/<slug:slug>', views.ProjectDetailView.as_view(), name='project-details'),
    path('blog', views.BlogListView.as_view(), name='blog'),
    path('blog/<slug:slug>', views.BlogDetailView.as_view(), name='blog-details'),
]
