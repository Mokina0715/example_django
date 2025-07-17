from django.urls import path
from django.views.generic import TemplateView
from myapp import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('cc_cacique', TemplateView.as_view(template_name='cc_cacique.html'), name='cc_cacique'),
    path('cc_laquinta', TemplateView.as_view(template_name='cc_laquinta.html'), name='cc_laquinta'),
    path('cc_megamall', TemplateView.as_view(template_name='cc_megamall.html'), name='cc_megamall'),
    path('centros_comerciales', views.lista_centros_comerciales, name='lista_centros_comerciales'),
]