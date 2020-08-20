from django.core.exceptions import ValidationError
from .models import Image
from django.forms import ModelForm, Form, CharField, NumberInput
from django.forms.widgets import URLInput, FileInput


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'url']
        widgets = {
            'image': FileInput(attrs={'class': 'form-control'}),
            'url': URLInput(attrs={'class': 'form-control'})
        }

    def clean(self):
        url = self.cleaned_data.get('url')
        if (self.files and url) or (not self.files and not url):
            raise ValidationError('Заполните только одно из полей', code='invalid')


class ImageDetailForm(Form):
    height = CharField(required=False, widget=NumberInput(attrs={'class': 'form-control'}))
    width = CharField(required=False, widget=NumberInput(attrs={'class': 'form-control'}))

    def clean(self):
        if not self.cleaned_data.get('height') and not self.cleaned_data.get('width'):
            raise ValidationError('Заполните одно из полей', code='invalid')