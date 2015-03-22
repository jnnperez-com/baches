from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from reportes.views import ReporteViewSet

router = DefaultRouter()
router.register(r'reporte', ReporteViewSet)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api', include(router.urls)), 
)
