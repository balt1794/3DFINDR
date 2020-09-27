from django.urls import path
from . import views

app_name = 'listings'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    # New Listing
    path('new_listing/', views.new_listing, name='new_listing'),
    # All Listings
    path('all_listings/', views.all_listings, name='all_listings'),
    # Detail of Individual Listing View
    path('all_listings/<detail_id>/', views.detail, name='detail'),
    # Edit Listing
    path('edit_listing/<detail_id>/', views.edit_listing, name='edit_listing'),
    # Delete Listing
    path('delete_listing/<detail_id>/',
         views.delete_listing, name='delete_listing'),
    # My Listings
    path('my_listings/', views.my_listings, name='my_listings'),
    # New Customer Profile
    path('profile/', views.profile, name='profile'),
    # My Profile
    path('my_profile/', views.my_profile, name='my_profile'),
    # Edit Profile
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    # Careers
    path('careers/', views.careers, name='careers'),
    # FAQ
    path('faq/', views.faq, name='faq'),



    # New Redesign Page
    path('new_index/', views.new_index, name='new_index'),
]
