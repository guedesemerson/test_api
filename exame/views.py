from rest_framework.generics import (
    ListAPIView,
    GenericAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from exame.serializers import (
    UpdateExameSerializer,
    RetrieveExameSerializer,
    ListExameSerializer,
    CreateExameSerializer
)
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from .models import Exame


class RegisterExameView(GenericAPIView):
    serializer_class = CreateExameSerializer

    def post(self, request):
        serializer = CreateExameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListExameView(ListAPIView):
    serializer_class = ListExameSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        'altura': ['gt']
    }

    def get_queryset(self):
        return Exame.objects.all()


class RetrieveExameView(RetrieveAPIView):
    serializer_class = RetrieveExameSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Exame.objects.filter(id=self.kwargs['id'])


class DeleteExameView(DestroyAPIView):
    lookup_field = "id"

    def get_queryset(self):
        queryset = Exame.objects.filter(id=self.kwargs['id'])
        return queryset

    def perform_destroy(self, instance):
        instance.delete()


class UpdateExameView(UpdateAPIView):
    serializer_class = UpdateExameSerializer
    lookup_field = 'id'

    def get_queryset(self):
        queryset = Exame.objects.filter(id=self.kwargs['id'])
        return queryset

    def perform_update(self, serializer):
        serializer.save()

