from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Medicine, Customer, Sale
from .forms import MedicineForm, CustomerForm, SaleForm
from rest_framework import viewsets
from .serializers import MedicineSerializer, CustomerSerializer, SaleSerializer

class MedicineListView(ListView):
    model = Medicine
    template_name = 'pharmacy/index.html'
    context_object_name = 'medicines'

class MedicineCreateView(CreateView):
    model = Medicine
    form_class = MedicineForm
    template_name = 'pharmacy/add_medicine.html'
    success_url = reverse_lazy('index')

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'pharmacy/add_customer.html'
    success_url = reverse_lazy('index')

class SaleCreateView(CreateView):
    model = Sale
    form_class = SaleForm
    template_name = 'pharmacy/sell_medicine.html'
    success_url = reverse_lazy('index')

class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer