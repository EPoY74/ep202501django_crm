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
    return render(request, 'client_detail.html',{'client' : client})



