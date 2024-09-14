"""
URL configuration for orderfood project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from website.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', web, name="web" ),
    path('success/', success, name='success'),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('success-page/', success_page, name="success_page"),
]
# from django.contrib import admin
# from django.urls import path
# from home.views import *
# from vege.views import *
# from django.conf.urls.static import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.conf import settings
# urlpatterns = [
#     path('', home),
#     path('recipes/', reciepe),
#     path('delete-reciepe/<id>/', delete_reciepe),
#     path('update-reciepe/<id>/', update_reciepe),
#     path('about/', about),
#     path('contact/', contact),
#     path('success-page/', success_page),
#     path('admin/', admin.site.urls),
#     #auth
#     path('login/', login_page),
#     path('register/', register),
#     path('logout/', logout_page),
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += staticfiles_urlpatterns()