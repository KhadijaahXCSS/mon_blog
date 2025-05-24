from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    derniers_articles = Article.objects.all().order_by('-date_creation')[:3]  
    return render(request, "pages/index.html", {'derniers_articles': derniers_articles})

def detail_article(request, id):
    article = Article.objects.get(id=id)
    return render(request, "articles/detail_article.html", {'article': article})
def articles(request):
    
    articles = Article.objects.all().order_by('-date_creation')
    paginator = Paginator(articles, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "articles/articles.html", {'articles': page_obj})

def mes_articles(request):
    if request.user.is_authenticated:
        articles = Article.objects.filter(auteur=request.user).order_by('-date_creation')
        paginator = Paginator(articles, 10)  
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "articles/mes_articles.html", {'articles': page_obj})
    else:
        return redirect('login')  




@login_required(login_url="/login/")
def ajout_article(request):
    if request.method == 'POST':
        titre = request.POST.get('titre')
        contenu = request.POST.get('contenu')
        
        
        article = Article(titre=titre, contenu=contenu, auteur=request.user)
        article.save()
        
        message = 'Article ajoute'
        return render(request, "articles/ajout_article.html", {'message': message})
    
    return render(request, "articles/ajout_article.html")


@login_required(login_url="/login/")
def modifier_article(request, id):
    article = get_object_or_404(Article, id=id)

    
    if article.auteur != request.user:
        return redirect('articles')  

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('detail_article', id=article.id)
    else:
        form = ArticleForm(instance=article)

    return render(request, 'articles/modifier_article.html', {'form': form, 'article': article})

@login_required(login_url="/login/")
def supprimer_article(request, id):
    article = get_object_or_404(Article, id=id)

    # Vérifier que l'utilisateur est l'auteur
    if article.auteur != request.user:
        return redirect('articles')  # ou return HttpResponseForbidden()

    article.delete()
    return redirect('articles')

