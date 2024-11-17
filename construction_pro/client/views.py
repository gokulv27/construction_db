from django.shortcuts import render, redirect
from .models import Client, Project
from django.db.models import Q

def client_list(request):
    search_query = request.GET.get('search', '')
    clients = Client.objects.filter(
        Q(client_lead_name__icontains=search_query) |
        Q(email__icontains=search_query)
    )
    return render(request, 'clients/client_list.html', {'clients': clients})

def add_client(request):
    if request.method == 'POST':
        # Create new client
        Client.objects.create(
            client_lead_name=request.POST['client_lead_name'],
            phone1=request.POST['phone1'],
            phone2=request.POST.get('phone2'),
            email=request.POST['email']
        )
        return redirect('client_list')
    return redirect('client_list')

def project_list(request, client_id):
    client = Client.objects.get(id=client_id)
    projects = client.projects.all()
    return render(request, 'clients/project_list.html', {'client': client, 'projects': projects})