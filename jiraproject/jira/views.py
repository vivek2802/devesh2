from django.shortcuts import get_object_or_404, render,redirect
from .models import Company,Project,Modules,user1
from django.views import generic
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View
from .form import userform1,moduleform
from django.contrib.auth.decorators import login_required,permission_required
from django.views.generic.list import ListView
from django.views.generic import DeleteView
from django.urls import reverse_lazy


from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .form import NameForm
from .form import Projectform
from django.views.generic.edit import UpdateView


#@login_required(login_url='/jira/^login/')
def index(request):
    company_list = Company.objects.all()
    context = {'company_list': company_list}
    return render(request, 'jira/index.html', context)
    # company = Company.objects.get(pk=company_id)
    # context1= {'company': company}
    # return render(request, 'jira/project.html',context1 )

@login_required(login_url='/jira/^login/')
@permission_required('jira.view_company',raise_exception=True)
def detail(request, company_id):
    company = Company.objects.get(pk=company_id)
    return render(request, 'jira/detail.html', {'company': company})

@login_required(login_url='/jira/^login/')
@permission_required('jira.reg',raise_exception=True)
def projectdetail(request, company_id):
    company = Company.objects.get(pk=company_id)
    return render(request, 'jira/project.html', {'company': company})

@login_required(login_url='/jira/^login/')
@permission_required('jira.reg',raise_exception=True)
def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            get_name = Company()
            get_name.company_name = form.cleaned_data.get('company_name', 'default1')
            get_name.company_address = form.cleaned_data.get('company_address', 'default2')
            get_name.company_description = form.cleaned_data.get('company_description', 'default3')
            get_name.company_code = form.cleaned_data.get('company_code', 'default3')
            get_name.save()
            return HttpResponse('Thanks')

    else:
        form = NameForm()

    return render(request, 'jira/name.html', {'form': form})

@login_required(login_url='/jira/^login/')
@permission_required('jira.reg',raise_exception=True)
def my_update(request , company_id):
    instance = get_object_or_404(Company, pk=company_id)
    form = NameForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponse('updated')
    return render(request, 'jira/name.html', {'form': form})

@login_required(login_url='/jira/^login/',)
@permission_required('jira.reg',raise_exception=True)
def delete(request , company_id):
    query = Company.objects.get(pk=company_id)
    query.delete()
    return HttpResponse("Deleted!")




@login_required(login_url='/jira/^login/')
@permission_required('jira.reg',raise_exception=True)
def get_project(request):
    if request.method == 'POST':
        form = Projectform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Thanks')

    else:
        form = Projectform()

    return render(request, 'jira/projectform.html', {'form': form})

#def employee(request):
  #  if request.method=='POST':
    #    form = employeeform(request.POST)
    #    if form.is_valid():
      #      form.save()
        #    return HttpResponse('employee added')

    #else:
     #   form = employeeform()
    #return render(request, 'jira/employee form.html', {'form': form})

#def employeelist(request):
   # employee_list = Employee.objects.all()
   # context = {'employee_list': employee_list}
    #return render(request, 'jira/employee.html', context)

#def edetail(request, employee_id):
    #employee = Employee.objects.get(pk=employee_id)
    #return render(request, 'jira/employee detail.html', {'employee': employee})

#def userformview(view):
 #   form_class= userform
  #  template_name='jira/registration.html'

   # def get(self,request):
    #    form=self.form_class(None)
     #   return render(request,self.template_name,{'form:form'})
    #def post(self,request):
     #   form= self.form_class(request.POST)

      #  if form.is_valid():
       #     user=form.save(commit=False)
        #    username=form.cleaned_data['username']
         #   password = form.cleaned_data['password']
          #  user.set_pasword(password)
           # user.save()

@login_required(login_url='/jira/^login/')
@permission_required('jira.reg',raise_exception=True)
def signup(request):
    if request.method == 'POST':
        form = userform1(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Thanks')

    else:
        form = userform1()

    return render(request, 'jira/user.html', {'form': form})

#def log_in(request):
  #  if request.method == 'POST':
   #     form = login(request.POST)
    #    username = request.POST.get('username',False)
     #   password = request.POST.get('password')
      #  user1 = authenticate(request, username=username, password=password)
       # return render(request, 'jira/login.html', {'form': form})


        #if user1 is not None:
         #   login(request, user1)
          #  return HttpResponseRedirect('/jira')
       #...
    #else:
     #   return HttpResponse('invalid input')

# # def login_view(request):
# #        username = request.POST['username']
# #        password = request.POST['password']
# #        user = authenticate(username=username, password=password)
# #        if user is not None and user.is_active:
# #            login(request, user)
# #            return HttpResponseRedirect("jira/")
#         else:
#             return HttpResponse('INVALID LOGIN')
@permission_required('jira.reg')
def get_modules(request):
    if request.method == 'POST':
        form = moduleform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Thanks')

    else:
        form = moduleform()

    print(form)

    return render(request, 'jira/moduleform.html', {'form': form})


class modules_list(ListView):
    model= Modules
    template_name='module_list.html'

    def get_queryset(self):

        x = self.kwargs['project_id']
        print(x)
        queryset = Modules.objects.filter(PROJECT_id= x)
        return queryset
 

class employee_list(ListView):
    model= user1


class project_delete(DeleteView):
    model = Project
    success_url = reverse_lazy('jira:index')


class project_update(UpdateView):
    model = Project
    fields = '__all__'
    success_url = reverse_lazy('jira:index')


class module_delete(DeleteView):
    model = Modules
    success_url = reverse_lazy('jira:index')

class module_update(UpdateView):
    model = Modules
    fields = '__all__'
    success_url = reverse_lazy('jira:index')