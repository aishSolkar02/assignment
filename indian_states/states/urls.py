
from django.urls import path
from .views import StateListView, StateDetailView, StateCreateView, StateUpdateView, StateDeleteView

urlpatterns = [
    path('', StateListView.as_view(), name='state_list'),
    path('state/<int:pk>/', StateDetailView.as_view(), name='state_detail'),
    path('state/create/', StateCreateView.as_view(), name='state_create'),
    path('state/<int:pk>/update/', StateUpdateView.as_view(), name='state_update'),
    path('state/<int:pk>/delete/', StateDeleteView.as_view(), name='state_delete'),
]
