from django import forms
#from.models import Post
from django.core.exceptions import ValidationError

#class ContactForm(forms.form):

#    your_surname = forms.CharField(max_length=100, label="Your surname")
#    your_name = forms.CharField(max_length=100, label="Your name")
#    your_secname = forms.CharField(max_length=100, label="Your secname")
#    mail = forms.CharField(max_length=100, label="Your mail")
#    describe = forms.CharField(widget=forms.Textarea(), label="Content")

#    def clean_subtitle(self):
#        title_data = self.cleaned_data['title']
#        subtitle_data = self.cleaned_data['subtitle']

#        if title_data == subtitle_data:
#            raise ValidationError("Title and subtitle shoul be different")
#        return subtitle_data