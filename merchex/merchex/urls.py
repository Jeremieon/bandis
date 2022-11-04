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
    path('bands/add/', views.band_create, name='band-create'),
    path('listing/add/', views.listing_create, name='list-create'),
    path('bands/<int:id>/change', views.band_update, name='band-update'),
    path('listing/<int:id>/change', views.listing_update, name='listing-update'),
    path('band/<int:id>/delete', views.band_delete, name='band-delete'),
    path('listing/<int:id>/delete',views.listing_delete, name='listing-delete')


]
