from django.urls import path

from app.views import *

urlpatterns = [
    path("", home, name="home"),
    path("hotels/", ItemListFilterByHotelView.as_view(), name="hotels"),
    path("tourist-attractions/", ItemListFilterByTouristAttractionView.as_view(), name="tourist_attractions"),
    path("concerts/", ItemListFilterByConcertView.as_view(), name="concerts"),
    path("amusement-parks/", ItemListFilterByAmusementParkView.as_view(), name="amusement_parks"),
    path("item/<int:pk>/", ItemView.as_view(), name="item_detail"),
    # path("item/<int:pk>/review", AddReviewView.as_view(), name="add_review"),
]
