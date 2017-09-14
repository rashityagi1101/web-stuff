from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login,name='login'),
    url(r'^login1/$', views.login1, name='login1'),
    url(r'^logout/$', views.logout, name='logut'),

    url(r'^material$',views.material,name='material' ),
    url(r'^index$',views.index,name='index'),

    url(r'^registerpage$', views.registerpage, name='registerpage'),
    url(r'^loginpage$', views.loginpage, name='loginpage'),
    url(r'^create_farmer$', views.create_farmer, name='create_farmer'),
    url(r'^create_retailer$', views.create_retailer, name='create_retailer'),
    url(r'^sell_crop$', views.sell_crop, name = 'sell_crop'),
    url(r'^farmer_dash$', views.farmer_dash, name='farmer_dash'),
    url(r'^complain$', views.complain, name='complain'),
    url(r'^complain_page$', views.complain_page, name='complain_page'),
    url(r'^ret_complain_page$', views.ret_complain_page, name='ret_complain_page'),

url(r'^cmp_status_farmer$', views.cmp_status_farmer, name='cmp_status_farmer'),
    url(r'^cmp_status_retailer/$', views.cmp_status_retailer, name='cmp_status_retailer'),

    url(r'^login/complain_page$', views.complain_page, name='complain_page'),
    url(r'^login1/ret_complain_page$', views.ret_complain_page, name='ret_complain_page'),
    url(r'^login/cmp_status_farmer$', views.cmp_status_farmer, name='cmp_status_farmer'),
    url(r'^login1/cmp_status_retailer/$', views.cmp_status_retailer, name='cmp_status_retailer'),

url(r'^register/complain_page$', views.complain_page, name='complain_page'),
    url(r'^register1/ret_complain_page$', views.ret_complain_page, name='ret_complain_page'),
    url(r'^register/cmp_status_farmer$', views.cmp_status_farmer, name='cmp_status_farmer'),
    url(r'^register1/cmp_status_retailer/$', views.cmp_status_retailer, name='cmp_status_retailer'),

    url(r'^create_farmer_extra$', views.create_farmer_extra, name='create_farmer_extra'),
    url(r'^register1/$', views.register1, name='register1'),
    url(r'^create_retailer_extra/$', views.create_retailer_extra, name='create_retailer_extra'),
    url(r'^retailer_dash/$', views.retailer_dash, name='retailer_dash'),
    url(r'^response_recv/$', views.response_recv, name='response_recv'),
    url(r'^rcomplain/$', views.rtcomplain, name='rcomplain'),
    url(r'^crop_details_farmer$', views.crop_details_farmer, name='crop_details_farmer'),
    url(r'^crop_ad_posted$', views.crop_ad_posted, name='crop_ad_posted'),
    url(r'^farmerlogoutt/$', views.farmerlogoutt, name='farmerlogoutt'),
    url(r'^retailerlogoutt/$', views.retailerlogoutt, name='retailerlogoutt'),
    url(r'^login/sell_crop$', views.sell_crop, name = 'sell_crop'),
]

