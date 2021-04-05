from django.contrib import admin
from django.urls import path, include
admin.site.site_header = 'Breach Check Admin'
admin.site.index_title = 'Administrator Panel'
admin.site.site_title = 'Breach Check Admin' 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
]
