from django.urls import path
from .views import PublicationListView, PublicationDetailView

urlpatterns = [
    path('', PublicationListView.as_view(), name='publication-list'),
    path( 'publication/<int:pk>/', PublicationDetailView.as_view(), name='publication-detail'), #(int:pk) es un parametro que se pasa a la vista y representa el numero de la llave primaria del objeto que se quiere ver   
    
]