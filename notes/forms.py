from django.core.exceptions import ValidationError
from django import forms
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'text':forms.Textarea
            (attrs={'class': 'form-control'}),
        }
        labels = {
            'text':'Write your thoughts here',
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' and 'django' not in title:
            raise ValidationError('We only accept notes about Django!')
        return title