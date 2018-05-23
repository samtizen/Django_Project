from django.conf.urls import url
from django.urls import include

from bootstrap_simple_note_app.ui.views import SimpleNoteListView, SimpleNoteLoginView, SimpleNoteCreateView, \
    SimpleNoteUpdateView, SimpleNoteSignUpView, SimpleNoteLogoutView, SimpleNoteUserListView, SimpleNoteDeleteView, \
    SimpleNoteUserProfile

urlpatterns = [
    url(r'^login/$', SimpleNoteLoginView.as_view(), name="login"),
    url(r'^signup/$', SimpleNoteSignUpView.as_view(), name="signup"),
    url(r'^logout/$', SimpleNoteLogoutView.as_view(), name="logout"),
    url(r'^profile/$', SimpleNoteUserProfile.as_view(), name="profile")
]

urlpatterns += [
    url('^', include('django.contrib.auth.urls')),
]

urlpatterns += [
    url(r'^$', SimpleNoteListView.as_view(), name="list"),
    url(r'^by-user/$', SimpleNoteUserListView.as_view(), name="user-list"),
    url(r'^(?P<pk>\d+)/$', SimpleNoteUpdateView, name="detail"),
    url(r'^create/$', SimpleNoteCreateView.as_view(), name="detail-create"),
    url(r'^(?P<pk>\d+)/update/$', SimpleNoteUpdateView.as_view(), name="detail-update"),
    url(r'^(?P<pk>\d+)/delete/$', SimpleNoteDeleteView.as_view(), name="detail-delete"),
]
