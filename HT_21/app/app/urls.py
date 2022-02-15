"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from goods.views import GoodsAPIView, CatAPIView

urlpatterns = [
    path('', include('goods.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/goodslist/', GoodsAPIView.as_view()),
    path('api/v1/goodslist/<int:pk>/', GoodsAPIView.as_view()),
    path('api/v1/category/', CatAPIView.as_view()),
    path('api/v1/category/<int:pk>/', CatAPIView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
