from rest_framework import serializers
from paciente.models import Paciente


class CreatePacienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Paciente
        fields = (
            'id',
            'nome',
            'idade',
            'endereco',
        )
        read_only_fields = [
            'id'
        ]


class ListPacienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Paciente
        fields = (
            'id',
            'nome',
            'idade',
            'endereco',
        )


class RetrievePacienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Paciente
        fields = (
            'id',
            'nome',
            'idade',
            'endereco',
        )


class UpdatePacienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Paciente
        fields = (
            'nome',
            'idade',
            'endereco',
        )

