from django.views.generic import TemplateView, CreateView, ListView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Customer, Medicine, Sale
from .forms import CustomerForm, MedicineForm, SaleForm, SaleItemFormSet

class IndexView(TemplateView):
    template_name = 'pharmacy/index.html'

class AddCustomerView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'pharmacy/add_customer.html'
    success_url = reverse_lazy('index')

class AddMedicineView(CreateView):
    model = Medicine
    form_class = MedicineForm
    template_name = 'pharmacy/add_medicine.html'
    success_url = reverse_lazy('index')

class SellMedicineView(CreateView):
    template_name = 'pharmacy/sell_medicine.html'
    success_url = reverse_lazy('index')

    def get(self, request):
        sale_form = SaleForm()
        formset = SaleItemFormSet()
        return render(request, self.template_name, {'sale_form': sale_form, 'formset': formset})

    def post(self, request):
        sale_form = SaleForm(request.POST)
        formset = SaleItemFormSet(request.POST)
        if sale_form.is_valid() and formset.is_valid():
            sale = sale_form.save()
            items = formset.save(commit=False)
            for item in items:
                item.sale = sale
                item.save()
                item.medicine.stock -= item.quantity
                item.medicine.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'sale_form': sale_form, 'formset': formset})

class InvoiceListView(ListView):
    model = Sale
    template_name = 'pharmacy/invoices.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        qs = super().get_queryset()
        if query:
            qs = qs.filter(customer__name__icontains=query) | qs.filter(customer__phone__icontains=query)
        return qs


from rest_framework import viewsets
from .models import Medicine, Customer, Sale, SaleItem
from .serializers import MedicineSerializer, CustomerSerializer, SaleSerializer

class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer