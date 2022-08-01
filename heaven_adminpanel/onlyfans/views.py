from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from .models import OnlyFansTable
from .forms import CreateOnlyfansTable
from users.models import Client,User


class OnlyFansWorkpage(View):

    template = 'onlyfans_template/workpage.html'

    def get(self, request):
        context = {
            'form': OnlyFansTable.objects.all(),
            'month': ( i for i in range(0,31))
        }
        return render(request, self.template, context)


class CreateNewTable(View):

    template = 'onlyfans_template/create_table.html'

    def get(self, request):
        context = {
            'form': CreateOnlyfansTable,
        }
        return render(request,self.template, context)

    def post(self, request):

        form = CreateOnlyfansTable(request.POST)
        if form.is_valid:
            if request.POST['table_type'] == '1':
                new_table = OnlyFansTable(
                    op=True, client=Client.objects.filter(id=int(request.POST['client']))[0],
                    operator=User.objects.filter(id=int(request.POST['operator']))[0])
                new_table.save()
            else:
                new_table = OnlyFansTable(
                   fp=True, pp=True, client=Client.objects.filter(id=int(request.POST['client']))[0],
                    operator=User.objects.filter(id=int(request.POST['operator']))[0])
                new_table.save()
        return redirect('onlyfans_workpage')

