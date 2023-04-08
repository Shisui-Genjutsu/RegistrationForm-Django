from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import User,model_relations,akatsukiteam,place


# Create your views here.
def template1(request):
    return render(request,'template1.html')
def footer1(request):
    return render(request,'footer1.html')
def model_relation(request):
    model1 = model_relations.objects.all()
    context = {'model1':model1}
    print(model1)
    return render(request,'model_relations.html',context)

#form1 views
def form1(request):
    if request.method == 'POST':
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            place = request.POST['place']
            purpose = request.POST['purpose']
            print(fname,lname,email,place,purpose)
            ins = akatsukiteam(fname=fname,lname=lname,email=email,place=place,purpose=purpose)
            ins.save()
    return render(request, 'form1.html',{})


def form1list(request):
    teammodel = akatsukiteam.objects.all()
    return render(request,'form1list.html',{'tm':teammodel})
  
def deleteform(request,myid):
    teammodeldelete = akatsukiteam.objects.get(id = myid)
    teammodeldelete.delete()
    return redirect('/form1')

def editform(request,myid):
    teammodeledit = akatsukiteam.objects.get(id = myid)
    teamfullmodeledit = akatsukiteam.objects.all()
    context = {
        'tme':teammodeledit,
        'tfme':teamfullmodeledit
    }
    return render(request,'form1.html',context)

def updateform(request,myid):
    tmu = akatsukiteam.objects.get(id = myid)
    tmu.fname = request.POST['fname']
    tmu.lname = request.POST['lname']
    tmu.email = request.POST['email']
    tmu.place = request.POST['place']
    tmu.purpose = request.POST['purpose']
    tmu.save()
    return redirect('/form1list')
    