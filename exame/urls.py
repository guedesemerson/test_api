from django.urls import path
from .views import (RetrieveExameView,
                    ListExameView,
                    RegisterExameView,
                    DeleteExameView,
                    UpdateExameView)

app_name = "api-exame"

urlpatterns = [
    path('register_exame', RegisterExameView.as_view(), name='register_exame'),
    path('list_exame', ListExameView.as_view(), name='list_exame'),
    path('retrieve_exame/<int:id>', RetrieveExameView.as_view(), name='retrieve_exame'),
    path('delete_exame/<int:id>', DeleteExameView.as_view(), name='delete_exame'),
    path('update_exame/<int:id>', UpdateExameView.as_view(), name='update_exame')
]