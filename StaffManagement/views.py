from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Staff
from .forms import StaffInsertForm
from django.contrib import messages










def ShowStaffInfo(request):
    all_Staff = Staff.objects.all()

    context={
        'all_staff': all_Staff
    }
    return render(request,'store/staff_list.html',context)







def GetStaffInfo(request):

    StaffForm = StaffInsertForm()

    if request.method == "POST":
        StaffForm = StaffInsertForm(request.POST)
        if StaffForm.is_valid():
            StaffForm.save()
            messages.info(request, 'Staff added successfully ✅')




    context={
        'form' : StaffForm
    }
    return render(request, 'store/create_staff.html',context)















