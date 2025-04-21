from django.urls import path
from .views import IndexView, AddCustomerView, AddMedicineView, SellMedicineView, InvoiceListView, InvoiceDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add-customer/', AddCustomerView.as_view(), name='add_customer'),
    path('add-medicine/', AddMedicineView.as_view(), name='add_medicine'),
    path('sell-medicine/', SellMedicineView.as_view(), name='sell_medicine'),
    path('invoices/', InvoiceListView.as_view(), name='invoice_list'),
    path('invoices/<int:pk>/', InvoiceDetailView.as_view(), name='invoice_detail'),
]