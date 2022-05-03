from django.db.models.query import QuerySet
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404

from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.db.models import Q
import datetime
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator
#from reportlab.pdfgen import canvas
#from reportlab.lib.pagesizes import letter
#from reportlab.lib.pagesizes import landscape
#from reportlab.platypus import Image
import os
from django.conf import settings
from django.http import HttpResponse
#from django.template.loader import get_template
#from xhtml2pdf import pisa
#from django.contrib.staticfiles import finders
import calendar
from calendar import HTMLCalendar
from DimosoApp.models import *
from DimosoApp.forms import *
#from hitcount.views import HitCountDetailView
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def base(request):
	return render(request, "DimosoApp/base.html")

def home(request):
	form = ContactForm(request.POST or None)
	expertise = Expertise.objects.all()
	experience = Experience.objects.all()
	skills = Skills.objects.all()
	summary = Summary.objects.all()
	myprojects = MyProject.objects.all()

	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			#hii user ananitumia mimi message
			email = request.POST.get('email')
			username = request.POST.get('username')
			phone = request.POST.get('phone')
			place = request.POST.get('place')
			body = request.POST.get('body')
			send_mail(username,body,settings.EMAIL_HOST_USER,[email], fail_silently=True)
			messages.success(request,"Message sent successfull to juniordimoso8@gmail.com")
			#zinaishia hapa

			#hizi mimi ndo namtumia user

			subject = f"Thanks {username} for visiting my website"
			message = f"Hey {username} you can communicate with me for more informations if you are ready!! Welcome"
			from_email = settings.EMAIL_HOST_USER
			recipient_list = [email]
			send_mail(subject,message,from_email,recipient_list, fail_silently=True)
			#zinaishia hapa
			return redirect('home')




	context ={
		"expertise":expertise,
		"experience":experience,
		"skills":skills,
		"summary":summary,
		"myprojects":myprojects,
		"form":form
	}

	return render(request, 'DimosoApp/home.html',context)


def detailpage(request,id):
	myprojects = MyProject.objects.get(id=id)
	context={
		"myprojects":myprojects
	}

	return render(request, "DimosoApp/detailpage.html",context)