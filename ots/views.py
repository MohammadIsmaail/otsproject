from django.shortcuts import render,loader
from django.http import HttpResponse,HttpResponseRedirect
from ots.models import *

def welcome(request):
    template=loader.get_template("welcome.html")
    res=template.render()
    return HttpResponse(res)

def candidateRegistrationForm(request):
    pass

def candidateRegistration(request):
    pass

def loginView(request):
    pass

def candidateHome(request):
    pass

def testPaper(request):
    pass

def calculateTestResult(request):
    pass

def testResultHistory(request):
    pass

def showTestResult(request):
    pass

def logoutView(request):
    pass
