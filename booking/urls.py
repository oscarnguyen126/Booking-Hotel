from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("booking_app.urls")),
    path("/user", include("user_manager.urls")),
]
