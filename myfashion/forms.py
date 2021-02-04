from django import forms
from .models import Post

        
# class AvisForm(forms.ModelForm):
#     class Meta:
#         model = Avis
#         fields = ['note']
#         widgets = {'note': forms.NumberInput(attrs={'class': 'Stars'})}
#         labels = {'note': 'Note /5'}
#         fields = ['commentaire']
#         widgets = {'commentaire': forms.Textarea(attrs={'class': 'form-control'})}