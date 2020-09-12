from django import forms

from .models import Upload


class UploadForm(forms.Form):
    class Meta:
        model = Upload
        fields = '__all__'


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(required=True)
    subject = forms.CharField()
    # phone = forms.CharField()
    message = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'placeholder': 'Enter Message Here', 'cols': "2", 'rows': "2",
               'class': ''}))
