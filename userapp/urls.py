from django.conf.urls import url
from .views import CricketerApiView

urlpatterns = [
    url(r'^$', CricketerApiView.as_view()),
]
