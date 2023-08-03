"""hykon_ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from apps.home.views import *

from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path("", include("apps.home.urls")),
    path("user/", include("apps.user.urls")),
    path("order/", include("apps.order.urls")),
    path("dashboard/", include("apps.dashboard.urls")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),


    path('oauth/', include('social_django.urls', namespace='social')),  # <-- here
    
]

if settings.DEBUG:
    urlpatterns.extend(
        [
            *static(
                settings.STATIC_URL,
                document_root=os.path.join(
                    settings.BASE_DIR, settings.STATICFILES_DIRS[0]
                ),
            ),
            *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
        ]
    )


