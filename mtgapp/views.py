from django.shortcuts import render
from .models import Card

# Create your views here.
def indexPageView(request):
    data = Card.objects.all()

    context = {
        "card" : data
    }
    return render(request, 'mtgapp/index.html', context)


def showSingleCardPageView(request, card_id):
    data = Card.objects.get(id = card_id)

    context = {
        "record" : data,
    }
    return render(request, 'mtgapp/editCard.html', context)


def updateCardPageView(request):
    if request.method == 'POST':
        card_id = request.POST['card_id']

        card = Card.objects.get(id=card_id)

        card.card_name = request.POST['card_name']
        card.color = request.POST['color']
        card.set = request.POST['set']
        card.rarity = request.POST['rarity']
        card.foil = request.POST['foil']
        card.extended = request.POST['extended']
        card.legendary = request.POST['legendary']
        card.quantity = request.POST['quantity']

        card.save()

    return indexPageView(request)


def deleteCardPageView(request, card_id):
    data = Card.objects.get(id=card_id)
    data.delete()

    return indexPageView(request)


def addCardPageView(request):
    if request.method == 'POST':

        card = Card()

        card.card_name = request.POST['card_name']
        card.color = request.POST['color']
        card.set = request.POST['set']
        card.rarity = request.POST['rarity']
        card.foil = request.POST['foil']
        card.extended = request.POST['extended']
        card.legendary = request.POST['legendary']
        card.quantity = request.POST['quantity']

        card.save()

        return indexPageView(request)
    else:
        return render(request, 'mtgapp/addCard.html')