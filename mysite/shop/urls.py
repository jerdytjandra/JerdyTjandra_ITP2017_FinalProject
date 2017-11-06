from django.conf.urls import url
from . import views

urlpatterns = [
	# /shop/
	url(r'^$', views.index, name='index'),

	# /shop/712/
	url(r'^(?P<pet_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^loginform', views.loginform),
	url(r'^login', views.Login),
	url(r'^logout', views.logout_view),
	url(r'^add/(?P<pet_id>[0-9]+)/$', views.addtocart),
	url(r'^cart/', views.cart),
	url(r'^checkout', views.checkout),
	url(r'^successful', views.successful)
]