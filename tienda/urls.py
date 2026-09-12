from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, ProductoViewSet, OrdenViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet, basename='categoria')
router.register(r'productos', ProductoViewSet, basename='producto')
router.register(r'ordenes', OrdenViewSet, basename='orden')

urlpatterns = router.urls
