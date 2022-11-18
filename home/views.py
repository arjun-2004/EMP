from django.shortcuts import render,redirect,HttpResponse
from home.models import Employee,Department,Role
from datetime import datetime



# Create your views here.
def index(request):
    return render(request,"index.html")
def all_emp(request):

    emp = Employee.objects.all()
    context={

        "emps":emp
    }
    # print(emp[1])
    return render(request,"all_emp.html",context)
def filter_emp(request):
    
        
    return render(request,"filter_emp.html")



def remove_emp(request,emp_id):
    if emp_id:

        try :

            instance = Employee.objects.get(id=emp_id)
            instance.delete()
            instance.save
            # return HttpResponse("the emp with id %s deleted successfully" % (emp_id))
            # return render(request,"all_emp.html")
            return redirect("all_emp")
        except:

            return render(request,"all_emp.html")
def add_emp(request):
    if request.method =="POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dept = int(request.POST.get('dept'))
        role = int(request.POST.get('role'))
        salary = int(request.POST.get('salary'))
        bonus = int(request.POST.get('bonus'))
        phone = int(request.POST.get('phone'))
        hireDate = datetime.today()
        print(first_name)
        new_emp = Employee(first_name=first_name,last_name=last_name,dept_id=dept,salary= salary,bonus=bonus,phone=phone,hireDate=hireDate,role_id=role)
        new_emp.save()
        return redirect("all_emp")
        
    else:
        return render(request,"add_emp.html")
