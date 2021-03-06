"""study_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

urlpatterns = [
    url(r'^simple-post-ui/', include('simple_post_ui_app.urls')),
    url(r'^simple-post-api/api/v1/', include('simple_post_api_app.api.urls')),
    url(r'^bootstrap-notes/', include(('bootstrap_simple_note_app.ui.urls', "bootstrap_simple_note_app"), namespace="bootstrap-note")),
    url(r'^bootstrap-notes/api/v1/', include('bootstrap_simple_note_app.api.v1.urls')),
]

urlpatterns += i18n_patterns(
    url(r'^admin/', admin.site.urls),
    prefix_default_language=True
)
