from django.conf.urls import url
from rest_framework.authtoken import views

from simple_post_api_app.api.views import simple_post_list_view, simple_post_detail_view, sign_up_view, SimplePostHTMLAPIView

urlpatterns = [
    url(r'^sign-up/$', sign_up_view),
    url(r'^sign-in/$', views.obtain_auth_token),
    url(r'^simple-posts/$', simple_post_list_view),
    url(r'^simple-posts/(?P<pk>\d+)/$', simple_post_detail_view),

    url(r'^simple-posts-html/$', SimplePostHTMLAPIView.as_view()),
]