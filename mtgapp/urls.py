from django.urls import path
from .views import indexPageView, showSingleCardPageView, updateCardPageView, deleteCardPageView, addCardPageView
from .views import addCardCardTypePageView, addCardCardSubTypePageView, addCardSubTypePageView, addSubPageView
from .views import deleteSubPageView, addCardSetPageView, addSetPageView, setPageView, deleteSetPageView
urlpatterns = [
    path("", indexPageView, name="index"),
    path("showCard/<int:card_id>/", showSingleCardPageView, name="showSingleCard"),
    path("updateCard/", updateCardPageView, name="updateCard"),
    path("deleteCard/<int:card_id>/", deleteCardPageView, name="deleteCard"),
    path("addCard/", addCardPageView, name="addCard"),
    path("addCardCardType/", addCardCardTypePageView, name="addCardCardType"),
    path("addCardCardSubType/", addCardCardSubTypePageView, name="addCardCardSubType"),
    path("subPage/", addCardSubTypePageView, name="subPage"),
    path("addSub/", addSubPageView, name="addSub"),
    path("deleteSub/<int:card_sub_type_id>/", deleteSubPageView, name="deleteSub"),
    path("addCardSet/", addCardSetPageView, name="addCardSet"),
    path("setPage/", setPageView, name="setPage"),
    path("addSet/", addSetPageView, name="addSet"),
    path("deleteSet/<int:set_id>/", deleteSetPageView, name="deleteSet"),
]
