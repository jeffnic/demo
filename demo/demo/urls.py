from django.conf.urls import url
from django.contrib import admin
from .views import home, demo, demo_delete

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^home/$', home, name='home'),
    url(r'^demo/$', demo, name='demo'),
    url(r'^demo_delete/(?P<id>\d+)/$', demo_delete, name='demo_delete'),
]
# (?P<order>\d+)


# url(r'^books/(?P<pk>\d+)/delete/$', views.book_delete, name='book_delete'),
