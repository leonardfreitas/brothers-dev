from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
# @ticket('RH_EMPLOYEE_CREATE')
def create(request):
    return render(request, 'employee_create.html')
