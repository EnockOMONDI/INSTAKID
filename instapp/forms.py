from django import forms
from .models import Image,Profile,Comment


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class UploadForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user','likes','upload_date','profile']
