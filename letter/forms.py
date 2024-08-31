from django import forms
from . models import Subscribers, MailMessage


class SubscibersForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ['email', ]
        
        widgets = {
            'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your email','style': 'text-align: center;', 'size':20}),
            }

        labels = {
            'email': '',  # Set label to empty string to remove it
        }

class MailMessageForm(forms.ModelForm):
    class Meta:
        model = MailMessage
        fields = ['title', 'message' ]
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the title'}),
            'message': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter the Message','rows': 4}),

            }
        
        labels = {
            'title': 'Message',     # Set label to empty string to remove it
            'message': '',   # Set label to empty string to remove it
        }