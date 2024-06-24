from django import forms

from .models import SendMessage

class SendMessageForm(forms.ModelForm):
    class Meta:
        model = SendMessage
        fields = '__all__'