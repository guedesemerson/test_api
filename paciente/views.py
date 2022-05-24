from rest_framework.generics import (
    ListAPIView,
    GenericAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from paciente.serializers import (
    UpdatePacienteSerializer,
    RetrievePacienteSerializer,
    ListPacienteSerializer,
    CreatePacienteSerializer
)
from rest_framework.response import Response
from rest_framework import status
from .models import Paciente


class RegisterPacienteView(GenericAPIView):
    serializer_class = CreatePacienteSerializer

    def post(self, request):
        serializer = CreatePacienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListPacienteView(ListAPIView):
    serializer_class = ListPacienteSerializer

    def get_queryset(self):
        return Paciente.objects.all()


class RetrievePacienteView(RetrieveAPIView):
    serializer_class = RetrievePacienteSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Paciente.objects.filter(id=self.kwargs['id'])


class DeletePacienteView(DestroyAPIView):
    lookup_field = "id"

    def get_queryset(self):
        queryset = Paciente.objects.filter(id=self.kwargs['id'])
        return queryset

    def perform_destroy(self, instance):
        instance.delete()


class UpdatePacienteView(UpdateAPIView):
    serializer_class = UpdatePacienteSerializer
    lookup_field = 'id'

    def get_queryset(self):
        queryset = Paciente.objects.filter(id=self.kwargs['id'])
        return queryset

    def perform_update(self, serializer):
        serializer.save()

