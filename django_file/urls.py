"""django_file URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page

from Upload import views
from cache1 import views as v
from django_file import settings

urlpatterns = [
                  url('admin/', admin.site.urls),
                  url('upload/', views.UploadView.as_view()),
                  url('index/', cache_page(10 * 60)(v.index)),
                  url('index1/', v.index1),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
