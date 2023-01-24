from django import forms
from django.forms import ModelForm
from django.forms import Textarea
#from.models import Post
from django.core.exceptions import ValidationError
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['your_surname', 'your_name', 'your_secname', 'mail', 'describe']
        widgets = {
            'describe': Textarea(
                attrs={
                    'placeholder': 'Ваше сообщение'
                }
            )
        }
#        your_surname = forms.CharField(max_length=100, label="Your surname")
#        your_name = forms.CharField(max_length=100, label="Your name")
#        your_secname = forms.CharField(max_length=100, label="Your secname")
#        mail = forms.EmailField(max_length=100, label="Your mail")
#        describe = forms.CharField(widget=forms.Textarea(), label="Content")

#    def clean_subtitle(self):
#        title_data = self.cleaned_data['title']
#        subtitle_data = self.cleaned_data['subtitle']
#        if title_data == subtitle_data:
#            raise ValidationError("Title and subtitle should be different")
#        return subtitle_data