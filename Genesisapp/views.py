from django.shortcuts import render, redirect, get_object_or_404

from Genesisapp.models import *

# Create your views here.
def details(request):
    return render(request, 'blog-details.html')

def blog(request):
    return render(request, 'blog.html')

def home(request):
    if request.method == 'POST':
        mycontact = Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            subjects=request.POST['subject'],
            message=request.POST['message']
        )
        mycontact.save()
        return render(request, 'index.html')
    
    else:
        return render(request, 'index.html')

def portfolio(request):
    return render(request, 'portfolio-details.html')

def service(request):
    return render(request, 'service-details.html')

def starter(request):
    return render(request, 'starter-page.html')

def delete(request, id):
    mycontact = Contact.objects.get(id=id)
    mycontact.delete()
    return redirect('/show')

def edit(request, id):
    editappointment = get_object_or_404(Contact, id=id)
    if request.method == 'POST':
        editappointment.name = request.POST['name']
        editappointment.email = request.POST['email']
        editappointment.subjects = request.POST['subject']
        editappointment.message = request.POST['message']
        editappointment.save()
        return redirect('/show')
    else:
        return render(request, 'edit.html', {'contact': editappointment})

def show(request):
   all = Contact.objects.all()
   return render(request, 'show.html', {'all': all})