from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .templates import form,model_form
from django.template import RequestContext
from .models import CnabFile
from django.db.models import Sum


def manage_file(request):
    file = form.FileForm(request.POST, request.FILES)
    if file.is_valid():
        model_form.data_processing(request)
        return redirect("/api/stores/")
    return render(request,"html/form.html",{"form":file})

def stores(request):
    stores = CnabFile.objects.all()

    stores_name = []
    store_name_value = []

    for name in stores:
        if name.store not in stores_name: 
            stores_name.append(name.store)
    for store_info in stores_name:
        store = CnabFile.objects.filter(store=store_info)[0]
        store_value = CnabFile.objects.filter(store=store_info).aggregate(total=Sum("value"))
        store.total = store_value["total"] / 100
        store_name_value.append(store)
    
    return render(request,"html/stores_list.html",{"stores":store_name_value})