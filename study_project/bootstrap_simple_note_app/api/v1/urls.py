from django.conf.urls import url

from bootstrap_simple_note_app.api.v1.views import SimpleNoteListAPIView

urlpatterns = [
    url(r'^notes/$', SimpleNoteListAPIView.as_view()),
]