from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from charity.models import charitydata


# Create your views here.

class charityList(ListView):
    model = charitydata

class charityView(DetailView):
    model = charitydata

class charityCreate(CreateView):
    model = charitydata
    fields = ['Charity_domain','Donor_name','Donation_date','Donation_amount']
    success_url = reverse_lazy('charity_list')

class charityUpdate(UpdateView):
    model =charitydata
    fields = ['Charity_domain','Donor_name','Donation_date','Donation_amount']
    success_url = reverse_lazy('charity_list')

class charityDelete(DeleteView):
    model = charitydata
    success_url = reverse_lazy('charity_list')

def charitydata_list(request):
    return render(request,'charity/charitydata_list.html',{})
