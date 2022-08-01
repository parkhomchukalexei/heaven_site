from django.contrib.auth import authenticate, login
from django.shortcuts import render, HttpResponse, redirect
from .forms import CreateClientForm

# Create your views here.
from django.views import View
from users.forms import UserCreationForm
from .models import Client


class Register(View):

    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')

        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class CreateClient(View):
    template_name = 'client/create_client.html'

    def get(self, request):
        form = CreateClientForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):

        form = CreateClientForm(request.POST)

        if form.is_valid:
            new_client = Client(name=form.data['name'], surname=form.data['surname'],
                   email=form.data['email'], login=form.data['login'],
                   password=form.data['password'], photo=form.data['photo'])
            new_client.save()
            return redirect('home')


class ClientList(View):

    template_name = 'client/client_list.html'

    def get(self, request):
        client_list = Client.objects.all()
        context = {'form': client_list}
        return render(request, self.template_name, context)


class ClientPage(View):

    template_name = 'client/client_page.html'

    def get(self, request, name):
        client = Client.objects.filter(name=name)
        context = {'form': client[0]}
        return render(request, self.template_name, context)


class DeleteClient(View):

    def get(self,request, client_id):
        client_to_delete = Client.objects.filter(id=client_id)
        client_to_delete.delete()
        return redirect('client_list')










