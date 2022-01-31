from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('employeelist/',views.EmployeeList.as_view()),
    path('employeelistcreate/',views.EmployeeListCreate.as_view()),
    # path('employeeretrieve/<int:pk>/',views.Employeeretrieve.as_view()),
    # path('employeeupdate/<int:pk>/',views.Employeeupdate.as_view()),
    # path('employeedestroy/<int:pk>',views.Employeedestroy.as_view()),
    # path('employeelistcreate/',views.Employeelistcreate.as_view()),
    # path('employeeretrieveupdate/<int:pk>/',views.Employeeretrieveupdate.as_view()),
    # path('employeeretrievedestroy/<int:pk>/',views.Employeeretrievedestroy.as_view()),
    path('employeeretrieveupdatedestroy/<int:pk>/',views.Employeeretrieveupdatedestroy.as_view()),
]
