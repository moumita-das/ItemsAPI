from django.conf.urls import url, include
from django.conf import settings

from django.conf.urls.static import static

from .views import CreateView,retrieveView,loginView


urlpatterns = [
    url(r'^login/$', loginView, name='login'),
    url(r'', loginView, name='create'),
    url('itemLists/create/',CreateView,name="create"),
    url('itemLists/retrieve/',retrieveView,name="retrieve"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
