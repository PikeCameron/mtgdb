from django.urls import path
from .views import indexPageView, showSingleCardPageView, updateCardPageView, deleteCardPageView, addCardPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("showCard/<int:card_id>/", showSingleCardPageView, name="showSingleCard"),
    path("updateCard/", updateCardPageView, name="updateCard"),
    path("deleteCard/<int:card_id>/", deleteCardPageView, name="deleteCard"),
    path("addCard/", addCardPageView, name="addCard"),
]
