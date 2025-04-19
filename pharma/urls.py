from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from pharmacy.views import MedicineViewSet, CustomerViewSet, SaleViewSet

router = routers.DefaultRouter()
router.register(r'medicines', MedicineViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'sales', SaleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pharmacy.urls')),
    path('api/', include(router.urls)),
]