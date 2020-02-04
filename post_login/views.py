from django.shortcuts import render

from pre_login.forms import LoginForm
from pre_login.forms import RegistrationForm
from pre_login.models import Personal_Details
from django.http import HttpResponseRedirect
from django.utils.datastructures import MultiValueDictKeyError


def student(request):
    information = Personal_Details.objects.all()
    print(information.get(Student="True"))
    info = Personal_Details.objects.get(Email=request.session['Email'])
    details = {"username" : info.username, "Age" : info.Age, "City":
    info.City, "State": info.State, "Country" : info.Country, "Occupation" : info.Occupation}
    return render(request,'quizes/student.html', details)

def project_m(request):
    info = Personal_Details.objects.get(Email=request.session['Email'])
    details = {"username" : info.username, "Age" : info.Age, "City":
    info.City, "State": info.State, "Country" : info.Country, "Occupation" : info.Occupation}
    return render(request,'quizes/project_m.html', details)

def student_details(request):
    information = Personal_Details.objects.all().filter(Student="True")
    print(information)
    diction = {'username' : []}
    for user in information:
        diction.get('username').append(user.username)
        print(diction)

    
    return render(request, 'quizes/list_stu.html', diction)

