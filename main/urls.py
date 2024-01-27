from django.urls import path


from .views import get_info_view, get_services_view, get_about_view, get_portfolio_view, get_testimonials_view, get_clients_view, get_contact_view, post_contact_view
urlpatterns = [
    path('get-info/', get_info_view),
    path('get-services/', get_services_view),
    path('get-about/', get_about_view),
    path('get-portfolio/', get_portfolio_view),
    path('get-testimonials/', get_testimonials_view),
    path('get-clients/', get_clients_view),
    path('get-contact/', get_contact_view),
    path('post-contact/', post_contact_view)
]

