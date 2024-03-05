from django.shortcuts import render
from django.http import HttpResponse,request,HttpResponseRedirect
from django.template import loader
from hubapp.models import Person
from .forms import NameForm

from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def homes(request):
    template=loader.get_template('index.html')
    context={'name':'ram'}
    return HttpResponse(template.render(context,request))

def persons(request):
    template=loader.get_template('person.html')
    # per=Person.objects.get(pk=1)
    per=Person.objects.all().values()
    context={
        'persons':per
        }
    return HttpResponse(template.render(context,request))

def perdetails(request,id):
    template=loader.get_template('perdetails.html')
    # per=Person.objects.get(pk=1)
    per=Person.objects.get(id=id)
    context={
        'person':per
        }
    return HttpResponse(template.render(context,request))

def main(request):
    template=loader.get_template('main.html')
    
    return HttpResponse(template.render())

def addperson(request):
    template=loader.get_template('addperson.html')
    
    return HttpResponse(template.render())



@csrf_exempt
def addpersoncreate(request):

    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        mob=request.POST['mob']
        dob=request.POST['dob']
        city=request.POST['city']
        state=request.POST['state']
        pin=request.POST['pin']

    print(fname,lname,email,mob,dob,city,state,pin)
    person=Person(fname=fname,lname=lname,email=email,mob=mob,dob=dob,city=city,state=state,pin=pin)
    person.save()
    template=loader.get_template('addsuccess.html')
    return HttpResponse(template.render())

def deleteperson(request, id):
    
    per = Person.objects.get(id=id)
    per.delete()
    template=loader.get_template('delete.html')
    return HttpResponse(template.render())



def update(request,id):
    template=loader.get_template('updateperson.html')
    person = Person.objects.get(id=id)
    context={
        'person':person
    }
    return HttpResponse(template.render(context,request))

def test(request):
    template=loader.get_template('test.html')
    person = Person.objects.all()
    context={
        'person':person,
        'fruits':['banana','mango','pomogranate','guava','apple','grapes','mango']
        
    }
    return HttpResponse(template.render(context,request))

def ffn(request):
    template=loader.get_template('test.html')
    person = Person.objects.filter(fname='enola')
    context={
        'person':person,
    }
    return HttpResponse(template.render(context,request))

def fln(request):
    template=loader.get_template('test.html')
    person = Person.objects.filter(lname='william')
    context={
        'person':person,
    }
    return HttpResponse(template.render(context,request))

def fc(request):
    template=loader.get_template('test.html')
    person = Person.objects.order_by('-fname')
    #order_by => arrange our data by descending order,we can use (-) for fname,lname anything
    context={
        'person':person,
    }
    return HttpResponse(template.render(context,request))

@csrf_exempt
def updateperson(request,id):

    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        dob=request.POST['dob']
        city=request.POST['city']
        state=request.POST['state']
        pin=request.POST['pin']

    person = Person.objects.get(id=id)
    person.fname=fname
    person.lname=lname
    person.dob=dob
    person.city=city
    person.state=state
    person.pin=pin
    person.save()
    context={
        'person':person
    }
    template=loader.get_template('updatesuccess.html')
    
    return HttpResponse(template.render())

# def homepage(request):
#     return render(request,'web.html')

# def python(request):
#     return HttpResponse("<h1>hello world this is pyhton django page with views and manage.we can create ,read ,update and delete operation in django which is known as CRUD operation.</h1>")

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/persons/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "user.html", {"form": form})