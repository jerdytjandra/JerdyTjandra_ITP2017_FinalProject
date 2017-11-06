from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^shop/', include('shop.urls')),
    url(r'^admin/', admin.site.urls),
]
