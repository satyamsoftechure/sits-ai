# forms.py
from django import forms
from .models import BlogPost, ReferenceBlogPost

class BlogGeneratorForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'keywords', 'language']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Topic or Title'}),
            'keywords': forms.TextInput(attrs={'placeholder': 'Keywords which you want to use'}),
            'language': forms.Select(choices=[('en', 'English'), ('hi', 'Hindi'), ('es', 'Spanish')], attrs={'default': 'en'}),
        }

    def __str__(self):
        return self.instance.title
    
class ReferenceBlogGeneratorForm(forms.ModelForm):
    class Meta:
        model = ReferenceBlogPost
        fields = ['title', 'keywords', 'reference', 'language', 'length']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Topic or Title'}),
            'keywords': forms.TextInput(attrs={'placeholder': 'Keywords which you want to use'}),
            'reference': forms.TextInput(attrs={'placeholder': 'Reference URL !'}),
            'language': forms.Select(choices=[('en', 'English'), ('hi', 'Hindi'), ('es', 'Spanish')], attrs={'default': 'en'}),
            'length': forms.NumberInput(attrs={'value': '1000', 'max': '1200'}),
        }

    def __str__(self):
        return self.instance.title
