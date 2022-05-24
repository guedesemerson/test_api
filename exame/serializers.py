from rest_framework import serializers
from paciente.models import Paciente
from exame.models import Exame


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'


class CreateExameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exame
        fields = (
            'id',
            'nome_profissional',
            'data_exame',
            'peso',
            'altura',
            'paciente',
        )
        read_only_fields = [
            'id'
        ]


class ListExameSerializer(serializers.ModelSerializer):
    paciente = PacienteSerializer(required=True)

    class Meta:
        model = Exame
        fields = (
            'id',
            'nome_profissional',
            'data_exame',
            'peso',
            'altura',
            'paciente',
        )


class RetrieveExameSerializer(serializers.ModelSerializer):
    paciente = PacienteSerializer(required=True)

    class Meta:
        model = Exame
        fields = (
            'id',
            'nome_profissional',
            'data_exame',
            'peso',
            'altura',
            'paciente',
        )


class UpdateExameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exame
        fields = (
            'nome_profissional',
            'data_exame',
            'peso',
            'altura',
            'paciente',
        )

