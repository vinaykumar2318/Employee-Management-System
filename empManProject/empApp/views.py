from django.shortcuts import render,HttpResponse
from .models import Employee
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(req):
    return render(req,'index.html')

def allEmp(req):
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    return render(req,'allEmp.html',context)

def addEmp(req):
    if req.method == 'POST':
        firstName = req.POST['firstName']
        lastName = req.POST['lastName']
        salary = int(req.POST['salary'])
        bonus = int(req.POST['bonus'])
        phone = int(req.POST['phone'])
        dept = int(req.POST['dept'])
        role = int(req.POST['role'])

        newEmp = Employee(firstName=firstName, lastName=lastName, salary=salary, bonus=bonus, phone=phone, dept_id=dept, role_id=role, hireDate=datetime.now())
        newEmp.save()
        return render(req,'index.html',{'added': True})
    elif req.method == 'GET':
        return render(req,'addEmp.html')
    else:
        return HttpResponse('<h1>An Error Occured</h1>')

def rmvEmp(req, empId=0):
    if empId:
        try:
            empToRmv = Employee.objects.get(id=empId)
            empToRmv.delete()
            return render(req,'index.html',{'removed': True})
        except:
            return HttpResponse('<h1>Please Enter a valid Employee Id</h1>')
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    return render(req,'rmvEmp.html', context)

def filEmp(req):
    if req.method == 'POST':
        firstName = req.POST.get('firstName', '').strip()
        lastName = req.POST.get('lastName','').strip()
        dept = req.POST['dept']
        role = req.POST['role']
        emps = Employee.objects.all()
        if firstName or lastName:
            emps = emps.filter(Q(firstName__icontains=firstName) & Q(lastName__icontains=lastName))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)

        context = {
            'emps':emps
        }
        return render(req, 'allEmp.html', context)
    elif req.method == 'GET':
        return render(req,'filEmp.html')
    else:
        return HttpResponse('<h1>An Error Occured</h1>')
