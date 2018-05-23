from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from bootstrap_simple_note_app.api.v1.serializers import SimpleNoteSerializer
from bootstrap_simple_note_app.models import SimpleNote

from datetime import datetime


class SimpleNoteListAPIView(ListAPIView):

    queryset = SimpleNote.objects.all()
    serializer_class = SimpleNoteSerializer

    def get_queryset(self):

        queryset = super().get_queryset()

        timestamp_param = self.request.GET.get("timestamp", None)

        if timestamp_param:
            datetime_timestamp = datetime.fromtimestamp(float(timestamp_param)).isoformat()
            print(datetime_timestamp)
            queryset = queryset.filter(updated__gt=datetime_timestamp)

        return queryset.order_by("-updated")

    def list(self, request, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        response_data = {
            "status": "OK",
            "notes": serializer.data,
            "timestamp": datetime.now().timestamp()
        }

        return Response(response_data)
