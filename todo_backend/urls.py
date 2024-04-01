from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/account/', include('user.urls')),
    path('api/v1/task/', include('task.urls')),
]
