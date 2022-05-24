from django.urls import path
from .views import (RegisterPacienteView,
                    ListPacienteView,
                    RetrievePacienteView,
                    DeletePacienteView,
                    UpdatePacienteView)

app_name = "api-paciente"

urlpatterns = [
    path('register_paciente', RegisterPacienteView.as_view(), name='register_paciente'),
    path('list_paciente', ListPacienteView.as_view(), name='list_paciente'),
    path('retrieve_paciente/<int:id>', RetrievePacienteView.as_view(), name='retrieve_paciente'),
    path('delete_paciente/<int:id>', DeletePacienteView.as_view(), name='delete_paciente'),
    path('update_paciente/<int:id>', UpdatePacienteView.as_view(), name='update_paciente')
]