from django.urls import path
from .views import CategoryModelViewSet, ProductModelViewSet
from rest_framework.routers import SimpleRouter, DefaultRouter

router = DefaultRouter()
router.register(r"product", ProductModelViewSet, basename="product")
router.register(r"category", CategoryModelViewSet, basename="category")
urlpatterns = router.urls

# urlpatterns = [
#     path('products/', ProductModelViewSet.as_view({"get": "list", "post": "create"})),
#     path('product/<int:pk>/', ProductModelViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}))
# ]
