from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
#..............

urlpatterns=[
#..............
url('^$',views.home,name='home'),
url(r'^profile/',views.profile, name='profile'),
url(r'^search/',views.search_results,name='search'),
url(r'^upload_image/',views.upload,name='upload'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
