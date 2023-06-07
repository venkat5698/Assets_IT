from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import AssetDetailsForm
import mysql.connector

@api_view(['POST'])
def asset_details(request):
    if request.method == 'POST':
        form = AssetDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return Response({'status': 'success'})
        else:
            return Response({'status': 'error', 'errors': form.errors})
    else:
        form = AssetDetailsForm()
        return render(request, 'assetdetails.html', {'form': form})
'''
import mysql.connector
m = mysql.connector.connect(
    host="localhost",
    user="root",
    database="bihy",
    password="1234",
)
print(m)
m.close()
'''