from django.contrib import admin
from .models import FAQ
from django_ckeditor_5.widgets import CKEditor5Widget
from django import forms

class FAQAdminForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = '__all__'
        widgets = {
            'answer': CKEditor5Widget(config_name='default'),
        }

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    form = FAQAdminForm