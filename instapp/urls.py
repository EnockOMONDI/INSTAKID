from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static
#..............

urlpatterns=[
#..............
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
