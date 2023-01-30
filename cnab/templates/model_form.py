from django import forms
from .form import File
from cnab import models

# class InsertFile(forms.ModelForm):
#   class Meta:
#     model = File
#     fields = [
#       'file'
#     ]


def data_processing(request):
    file = request.FILES["file"]

    for info in file:
        separate_info = info.decode()

        data = {
            "type": separate_info[0],
            "date": separate_info[1:9],
            "value": separate_info[9:19],
            "cpf": separate_info[19:30],
            "credit_card": separate_info[30:42],
            "hour": separate_info[42:48],
            "owner": separate_info[48:62],
            "store": separate_info[62:80],
        }
        if data["type"] == "2" or data["type"] == "3" or data["type"] == "9":
          data["value"] = "-"+data["value"]

        instance = models.CnabFile.objects.create(**data)
        instance.save()