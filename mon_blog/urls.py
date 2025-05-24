from django.urls import path
from .views import home,detail_article,articles,mes_articles,ajout_article,modifier_article,supprimer_article
urlpatterns = [
    path("",home,name="index"),
    path("articles/",articles,name="articles"),
    path("articles/<int:id>/",detail_article,name="detail_article"),
    path ("articles/mes_articles/",mes_articles,name="mes_articles"),
    path ("articles/ajout_article/",ajout_article,name="ajout_article"),
    path ("articles/modifier_article/<int:id>/",modifier_article,name="modifier_article"),
    path('articles/supprimer_article/<int:id>/', supprimer_article, name='supprimer_article'),

    
]