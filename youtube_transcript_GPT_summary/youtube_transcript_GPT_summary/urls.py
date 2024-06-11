from django.contrib import admin
from django.urls import path
from summary_generator.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
]
