from django.urls import path
from .views import (
                    PublicationListView, 
                    PublicationDetailView, 
                    PublicationCreateView,
                    PublicationUpdateView
                    )

urlpatterns = [
    path('', PublicationListView.as_view(), name='publication-list'),
    path( 'publication/<int:pk>/', PublicationDetailView.as_view(), name='publication-detail'), #(int:pk) es un parametro que se pasa a la vista y representa el numero de la llave primaria del objeto que se quiere ver   
    path('publication/new/', PublicationCreateView.as_view(), name='publication-create'),
    path('publication/<int:pk>/update/', PublicationUpdateView.as_view(), name='publication-update'),
]