from django.urls import path
from django.views.generic import TemplateView
from myapp import views

urlpatterns = [
    path('home', TemplateView.as_view(template_name='index.html'), name='index'),
    path('cc_cacique', TemplateView.as_view(template_name='cc_cacique.html'), name='cc_cacique'),
    path('cc_laquinta', TemplateView.as_view(template_name='cc_laquinta.html'), name='cc_laquinta'),
    path('cc_megamall', TemplateView.as_view(template_name='cc_megamall.html'), name='cc_megamall'),
    # path('centros_comerciales', views.lista_centros_comerciales, name='lista_centros_comerciales'),
    path('', views.lista_centros_comerciales, name='lista_centros_comerciales'),
    path('tiendas', views.lista_centros_tiendas, name='lista_centros_tiendas'),
    path('cc/<str:name_cc>', views.vista_centros_comercial, name='vista_centros_comercial' ),
]