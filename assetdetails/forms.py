from django import forms
from .models import AssetDetails

class AssetDetailsForm(forms.ModelForm):
    class Meta:
        model = AssetDetails
        fields = ['employee_name', 'employee_id', 'gender', 'asset_id', 'system_type', 'designation', 'mobile_number', 'imei_number', 'dongle_number', 'date', 'start_date', 'end_date', 'filename']