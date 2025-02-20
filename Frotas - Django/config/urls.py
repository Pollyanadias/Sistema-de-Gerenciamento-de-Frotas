"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from frotas.api.views import FrotaViewSet, MotoristaViewSet, VeiculoViewSet, RastreamentoViewSet, ManutencaoViewSet, AlocacaoViewSet, EventoTelemetriaViewSet, AdvertenciaMotoristaViewSet
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from users.api.views import UserProfileExampleViewSet

router = SimpleRouter()

router.register("users", UserProfileExampleViewSet, basename="users")
router.register("frotas", FrotaViewSet, basename="frotas")
router.register("veiculos", VeiculoViewSet, basename="veiculos")
router.register("motoristas", MotoristaViewSet, basename="motoristas")
router.register("rastreamentos", RastreamentoViewSet, basename="rastreamentos")
router.register("manutencoes", ManutencaoViewSet, basename="manutencoes")
router.register("alocacoes", AlocacaoViewSet, basename="alocacoes")
router.register("eventos", EventoTelemetriaViewSet, basename="eventos")
router.register("advertencias", AdvertenciaMotoristaViewSet, basename="advertencias")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token-auth/", views.obtain_auth_token),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]+router.urls
