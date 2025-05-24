from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    resume = models.TextField(blank=True, null=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.titre} ({self.auteur.username})"
    
    
    def resume(self):
        return self.contenu[:150] + "..." if len(self.contenu) > 150 else self.contenu