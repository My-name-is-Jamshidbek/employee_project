from django.shortcuts import render, redirect
from .form import EmployeeForm
from .models import Position, Employee

# Create your views here.

def _list(request):
    employee_list = Employee.objects.all()
    context = {'employee_list': employee_list}
    
    return render(request, 'register/list.html', context)


def _form(request):
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee')
        
    positions = Position.objects.all()
    form = EmployeeForm()
    context = {'positions': positions, 'form': form}
    
    return render(request, 'register/form.html', context)


def _positions(request):
    positions = Position.objects.all()
    
    if request.method == 'POST':
        position_name = request.POST.get('position_name')
        Position.objects.create(
            title = position_name,
        )
    
    context = {'positions': positions,}
    
    return render(request, 'register/positions.html', context)


def _del(request, pk):

    Employee.objects.filter(pk=pk).delete()

    return redirect('employee')


def _edit(request, pk):
    employee = Employee.objects.get(pk=pk)

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee')
        
    positions = Position.objects.all()
    form = EmployeeForm()
    context = {'positions': positions, 'form': form, "old_form": employee}
    
    return render(request, 'register/edit.html', context)
    