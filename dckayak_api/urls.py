"""dckayak_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles import views
from django.views.generic import TemplateView
from . import settings
from usgsflows.views import FlowListView, FlowViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('flows', FlowViewSet)

admin.site.site_header = settings.ADMIN_SITE_HEADER

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
    # url(r'^posts', TemplateView.as_view(template_name="mediaposts/media_home.html"), name="media_main"),
    # url('flows/', FlowListView.as_view(), name="flow-list"),
    # url(r'^admin/password_reset/$', auth_views.password_reset, name='admin_password_reset'),
    # url(r'^admin/password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', auth_views.password_reset_confirm,
    #     name='password_reset_confirm'),
    # url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    # # url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url('admin/', admin.site.urls),
    url('api/',  include(router.urls))
]