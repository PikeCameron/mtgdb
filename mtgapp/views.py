from django.shortcuts import render
from .models import Card, Card_Type, Card_Sub_Type, Set

# Create your views here.
def indexPageView(request):
    data = Card.objects.all()

    context = {
        "card" : data,
    }
    return render(request, 'mtgapp/index.html', context)


def showSingleCardPageView(request, card_id):
    data = Card.objects.get(id = card_id)
    card_type = data.card_type.all()
    card_sub_type = data.card_sub_type.all()
    set = data.set.all()
    rare = data.rarity
    avail_type = Card_Type.objects.exclude(id__in=data.card_type.all())
    avail_sub_type = Card_Sub_Type.objects.exclude(id__in=data.card_sub_type.all())
    avail_set = Set.objects.exclude(id__in=data.set.all())

    context = {
        "record" : data,
        "type" : card_type,
        "sub_type" : card_sub_type,
        "set" : set,
        "rarity" : rare,
        "avail" : avail_type,
        "avail2" : avail_sub_type,
        "avail3" : avail_set,
    }
    return render(request, 'mtgapp/editCard.html', context)


def updateCardPageView(request):
    if request.method == 'POST':
        card_id = request.POST['card_id']

        card = Card.objects.get(id=card_id)

        card.card_name = request.POST['card_name']
        card.color = request.POST['color']
        card.rarity = request.POST['rarity']
        card.foil = request.POST['foil']
        card.extended = request.POST['extended']
        card.retro = request.POST['retro']
        card.legendary = request.POST['legendary']
        card.quantity = request.POST['quantity']

        card.save()

    return showSingleCardPageView(request, card_id)


def deleteCardPageView(request, card_id):
    data = Card.objects.get(id=card_id)
    data.delete()

    return indexPageView(request)


def addCardPageView(request):
    if request.method == 'POST':

        card = Card()

        card.card_name = request.POST['card_name']
        card.color = request.POST['color']
        card.rarity = request.POST['rarity']
        card.foil = request.POST['foil']
        card.extended = request.POST['extended']
        card.retro = request.POST['retro']
        card.legendary = request.POST['legendary']
        card.quantity = request.POST['quantity']

        card.save()

        return showSingleCardPageView(request, card.id)
    else:
        return render(request, 'mtgapp/addCard.html')


def addCardCardTypePageView(request):
    if request.method == 'POST':
        card_id = request.POST['card_id']
        card = Card.objects.get(id=card_id)

        type = request.POST['card_type']
        card.card_type.add(Card_Type.objects.get(id=type))
    return showSingleCardPageView(request, card_id)

def addCardCardSubTypePageView(request):
    if request.method == 'POST':
        card_id = request.POST['card_id']
        card = Card.objects.get(id=card_id)

        sub_type = request.POST['card_sub_type']
        card.card_sub_type.add(Card_Sub_Type.objects.get(id=sub_type))
    return showSingleCardPageView(request, card_id)

def addCardSetPageView(request):
    if request.method == 'POST':
        card_id = request.POST['card_id']
        card = Card.objects.get(id=card_id)

        title = request.POST['card_set']
        card.set.add(Set.objects.get(id=title))
    return showSingleCardPageView(request, card_id)

def addCardSubTypePageView(request):
    card_sub_type = Card_Sub_Type.objects.all()

    context = {
        "sub_type" : card_sub_type,
    }
    return render(request, 'mtgapp/subPage.html', context)

def addSubPageView(request):
    if request.method == 'POST':
        sub = Card_Sub_Type()

        sub.sub_type = request.POST['sub_type']

        sub.save()

        return addCardSubTypePageView(request)
    else:
        return render(request, 'mtgapp/addSub.html')

def deleteSubPageView(request, card_sub_type_id):
    data = Card_Sub_Type.objects.get(id=card_sub_type_id)
    data.delete()

    return addCardSubTypePageView(request)


def setPageView(request):
    set = Set.objects.all()

    context = {
        "set" : set,
    }
    return render(request, 'mtgapp/setPage.html', context)

def addSetPageView(request):
    if request.method == 'POST':
        set = Set()

        set.title = request.POST['set']

        set.save()

        return setPageView(request)
    else:
        return render(request, 'mtgapp/addSet.html')

def deleteSetPageView(request, set_id):
    data = Set.objects.get(id=set_id)
    data.delete()

    return setPageView(request)