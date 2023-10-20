from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('handbook/', include("handbook.urls")),
    path('admin/', admin.site.urls),
]
