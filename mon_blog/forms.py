from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'contenu']  
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre de l\'article'}),
            'contenu': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Contenu complet de l\'article', 'rows': 6}),
            
        }
