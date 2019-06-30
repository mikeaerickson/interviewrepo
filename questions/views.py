# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Job, Question



def home(request):
    jobs=Job.objects.all()

    return render(request, 'home.html',{'jobs':jobs})


def interview(request, shortname):
	job=Job.objects.get(short=shortname)
	questions = Question.objects.filter(belongs_to=job).order_by('?')

	return render(request, 'interview.html',{'job':job, 'questions':questions})	

