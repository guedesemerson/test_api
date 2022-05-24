from django.urls import include, path
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Test Api",
        default_version='v1',
        description="Builded by Emerson Guedes de Oliveira",
        contact=openapi.Contact(email="guedes.emerson@hotmail.com"),
        license=openapi.License(name="Todos os direitos reservados: Advertise here"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("v1/paciente/", include("paciente.urls", namespace='api-user')),
    path("v1/exame/", include("exame.urls", namespace='api-exame')),
    path("admin/", admin.site.urls),
    path("", schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]