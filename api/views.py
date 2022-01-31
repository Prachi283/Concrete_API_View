from .models import Employee
from .serializers import EmployeeSerializer
"""
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView

class EmployeeList(ListAPIView):
	queryset=Employee.objects.all()
	serializer_class=EmployeeSerializer

class EmployeeCreate(CreateAPIView):
	queryset=Employee.objects.all()
	serializer_class=EmployeeSerializer

class Employeeretrieve(RetrieveAPIView):
	queryset=Employee.objects.all()
	serializer_class=EmployeeSerializer

class Employeeupdate(UpdateAPIView):
	queryset=Employee.objects.all()
	serializer_class=EmployeeSerializer

class Employeedestroy(DestroyAPIView):
	queryset=Employee.objects.all()
	serializer_class=EmployeeSerializer

class Employeelistcreate(ListCreateAPIView):
	queryset=Employee.objects.all()
	serializer_class=EmployeeSerializer

class Employeeretrieveupdate(RetrieveUpdateAPIView):
	queryset=Employee.objects.all()
	serializer_class=EmployeeSerializer

class Employeeretrievedestroy(RetrieveDestroyAPIView):
	queryset=Employee.objects.all()
	serializer_class=EmployeeSerializer

class Employeeretrieveupdatedestroy(RetrieveUpdateDestroyAPIView):
	queryset=Employee.objects.all()
	serializer_class=EmployeeSerializer

"""

# Optional Code 

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class EmployeeListCreate(ListCreateAPIView):
	queryset=Employee.objects.all()
	serializer_class=EmployeeSerializer

class Employeeretrieveupdatedestroy(RetrieveUpdateDestroyAPIView):
	queryset=Employee.objects.all()
	serializer_class=EmployeeSerializer
