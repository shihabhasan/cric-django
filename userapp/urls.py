from django.conf.urls import url
from .views import CricketerApiView, CricketRunApiView, CricketSummaryApiView

urlpatterns = [
    url(r'^$', CricketerApiView.as_view()),
    url(r'^run$', CricketRunApiView.as_view()),
    url(r'^summary$', CricketSummaryApiView.as_view()),
]
