from rest_framework import serializers

from bootstrap_simple_note_app.models import SimpleNote


class SimpleNoteSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = SimpleNote
        fields = "__all__"