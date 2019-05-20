from django.shortcuts import render
from django.http import Http404
from pages.models import Article
from .forms import ContactForm

def contact(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = ContactForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid():
        # Ici nous pouvons traiter les données du formulaire
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']

        # Nous pourrions ici envoyer l'e-mail grâce aux données
        # que nous venons de récupérer
        envoi = True

    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'pages/contact.html', locals())

def accueil(request):
    """ Afficher tous les articles de notre blog """
    articles = Article.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'pages/accueil.html', {'derniers_articles': articles})

def lire(request, id):
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404

    return render(request, 'pages/lire.html', {'article': article})


#
#def pageif(request):
#    context={'age':19}
#    return render(request, "pages/pageif.html", context)
#
#def pagefor(request):
#    context = {'maliste': ["Younes", "Geoffrey", "Larry", "Kasim", "Yassine", "Adam", "Jason", "Pamela", "Isac", "Jeremy", "Mehmet", "Jinane"]}
#    return render(request, "pages/pagefor.html", context)

