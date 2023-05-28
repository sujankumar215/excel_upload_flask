from django.urls import path
from finance.views import feeDuesReport,feeCollection,feeCollectionReport
urlpatterns = [
 
    
    path('feecall/', feeCollection),
    path('collreport/', feeCollectionReport),
    path('duesreport/', feeDuesReport),
]
