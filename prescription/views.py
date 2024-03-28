from django.shortcuts import render
from prescription.models import Prescription

from django.contrib import messages
# Create your views here.

def prescrip(request):
    # return render (request, 'upload.html')

# def prescription(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        contactnum = request.POST.get('contactnum')
        image = request.POST.get('image')

        pres = Prescription(fullname = fullname, contactnum = contactnum, image = image)
        pres.save()
        messages.success(request, 'Thankyou.. Your Prescription Submitted Successfuly...')
    return render(request, 'upload.html')


