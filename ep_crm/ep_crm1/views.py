"""Создаю формы и представления для данных"""
# Create your views here.
from django.shortcuts import render, get_object_or_404
from ep_crm1.models import Client  #, Task, Deal
# from .forms import ClientForm, DealForm, TaskForm

def clients_list(request):
    """вывожу список клиентов"""
    clients = Client.objects.all()
    return render(request, 'clients_list.html', {'clients' : clients})


def client_detail(request, pk):
    """Вывожу детали по клиенту"""
    client=get_object_or_404(Client,pk=pk)
    verbose_names = {}
    for field in Client._meta.get_fields():
        if hasattr(field, 'verbose_name'):
            verbose_names[field.name] = field.verbose_name
            table_name = Client._meta.verbose_name
    return render(request, 'client_detail.html',
                  {'client' : client,
                    'verbose_names' : verbose_names,
                    'table_name' : table_name,
                    })



