from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from jira.views import modules_list,employee_list,project_delete,project_update,module_delete,module_update


app_name = "jira"

urlpatterns = [
    path('admin/', admin.site.urls),

    path('<int:company_id>/', views.detail, name='detail'),
    path('<int:company_id>/project', views.projectdetail, name='projectdetail'),
    path('Addcompany/', views.get_name, name='addcompany'),
    path('<int:company_id>/Update', views.my_update, name='update'),
    path('<int:company_id>/delete', views.delete, name='delete'),
    path('Addproject/', views.get_project, name='project'),
    #path('Addemployee/',views.employee,name='employee form'),
    path('employee/',employee_list.as_view(),name='employees'),
   # path('employee/<int:employee_id>/',views.edetail,name='empdetail'),
    path('userreg',views.signup,name='reg'),
    #path('login',views.login_view,name='login'),
    path('login/', auth_views.login, {'template_name': 'jira/login.html'},name='login'),

    path('logout/', auth_views.logout, name='logout'),
    path('module/',views.get_modules,name='module'),
    path('', views.index, name='index'),
    path('<int:project_id>/modules/', modules_list.as_view(),name='modulelist'),
    path('delete/<int:pk>/', project_delete.as_view(),name='project delete'),
    path('update/<int:pk>/', project_update.as_view(),name='project delete'),
    path('deletemodule/<int:pk>/',module_delete.as_view(),name='module delete'),
    path('updatemodule/<int:pk>/',module_update.as_view(),name='module delete')




]
