from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def feeCollection(request):
    return render(request,'finance/feeCollection.html')

@login_required
def feeDuesReport(request):
    return render(request,'finance/feeDueReport.html')
    #return HttpResponse("<h1>I will fiew Due report from this view</h1>")

@login_required
def feeCollectionReport(request):
    return render(request,'finance/feeCollectReport.html')
    #return HttpResponse("<h1>I will view collect report from this view</h1>")



