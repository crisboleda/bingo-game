
from django.contrib import admin
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path('api/v1/', include('bingo_api.urls')),
    path('admin/', admin.site.urls),
]
