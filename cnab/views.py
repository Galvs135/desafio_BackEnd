from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .templates import form,model_form
from django.template import RequestContext
from .models import CnabFile
from django.db.models import Sum


def manage_file(request):
    print(request.FILES)
    file = form.FileForm(request.POST, request.FILES)
    if file.is_valid():
        model_form.data_processing(request)
        return redirect("/api/stores/")
    return render(request,"form.html",{"form":file})



# class manage_files(CreateView):
#     template_name = "form.html"
#     model = form.FileForm
#     form_class = model_form.InsertFile
#     success_url = reverse_lazy("file")

#     def manage_file(request):
#         file = model_form.InsertFile(request.POST, request.FILES)
        
#         if file.is_valid():
#             model_form(request)


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
    
    return render(request,"stores_list.html",{"stores":store_name_value})