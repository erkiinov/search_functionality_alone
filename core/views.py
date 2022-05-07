from multiprocessing import context
from django.shortcuts import render
from .models import Employers
from django.db.models import Q

def home(request):
    if 'q' in request.GET:
        Search_word = request.GET['q']
        Full = Q(Q(first_name__icontains=Search_word) | Q(second_name__icontains=Search_word) | Q(age__icontains=Search_word) | Q(job__icontains=Search_word))
        Employer = Employers.objects.filter(Full)
    else:
        Employer = Employers.objects.all()

    context = {
        'Employers' : Employer
    }
    return render(request, 'index.html', context)