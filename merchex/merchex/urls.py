from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('bands/',views.band_list,name='band_list'),
    path('bands/<int:id>/', views.band_detail, name='band-detail'),
    path('about-us/',views.about,name='email-sent'),
    path('listing/',views.listing_view,name='listing_view'),
    path('listing/<int:id>/', views.listing_detail, name='listing_detail'),
    path('contact-us/',views.contact,name='contact'),

]
