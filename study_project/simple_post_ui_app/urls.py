from django.conf.urls import url

from . import views

urlpatterns = [

    # ===================================
    # Response, Context, Template
    # ===================================

    # view 1
    url(r'^http-response/$', views.view_http_response, name="testapp_view-http-response"),

    # view 2
    url(r'^http-response_with_var/$',
        views.view_http_response_with_var,
        name="testapp_view-http-response-with-var"),

    # view 3
    url(r'^http-response_with_template/$',
        views.view_http_response_with_template,
        name="testapp_view-http-response-with-template"),
    # view 4
    url(r'^http-response_with_template_var/$',
        views.view_http_response_with_template_var,
        name="testapp_view-http-response-with-template-var"),
    # view 5
    url(r'^http-response_with_template_var_2/$',
        views.view_http_response_with_template_var_2,
        name="testapp_view-http-response-with-template-var-2"),
    # view 6
    url(r'^http-redirect/$',
        views.view_http_redirect,
        name="testapp_view-http-redirect"),
    # view 7
    url(r'^json-response/$',
        views.view_json_response,
        name="testapp_view-json-response"),

    # ===================================
    # Template with static files
    # ===================================

    # view 8
    url(r'^http-response-with-static/$',
        views.view_http_response_with_static,
        name="testapp_view-http-response-with-static"),

    # ===================================
    # Parameters - URL, GET, POST
    # ===================================

    # view 9
    url(r'^http-response-url-args/$',
        views.view_http_response_url_args,
        name="testapp_view-http-response-url-args"),
    url(r'^http-response-url-args/([+ \w]+)/$',
        views.view_http_response_url_args,
        name="testapp_view-http-response-url-args"),
    url(r'^http-response-url-args/([+ \w]+)/([+ \w]+)/$',
        views.view_http_response_url_args,
        name="testapp_view-http-response-url-args"),

    # view 10
    url(r'^http-response-url-kwargs/$',
        views.view_http_response_url_kwargs,
        name="testapp_view-http-response-url-kwargs"),
    url(r'^http-response-url-kwargs/(?P<header>[+ \w]+)/$',
        views.view_http_response_url_kwargs,
        name="testapp_view-http-response-url-kwargs"),
    url(r'^http-response-url-kwargs/(?P<header>[+ \w]+)/(?P<content>[+ \w]+)/$',
        views.view_http_response_url_kwargs,
        name="testapp_view-http-response-url-kwargs"),

    # view 11
    url(r'^http-response-get-post/$',
        views.view_http_response_get_post,
        name="testapp_view-http-response-get-post"),

    # ===================================
    # Models
    # ===================================

    # create
    url(r'^create/$',
        views.create_simple_post,
        name="testapp_create-simple-post"),
    # select all
    url(r'^$',
        views.simple_post_list_view,
        name="testapp_simple-post-list"),
    # select by id
    url(r'^(?P<pk>\d+)/$',
        views.simple_post_list_view,
        name="testapp_simple-post-list"),
    # update
    url(r'^(?P<pk>\d+)/update$',
        views.update_simple_post,
        name="testapp_update-simple-post"),
    # delete
    url(r'^(?P<pk>\d+)/delete',
        views.delete_simple_post,
        name="testapp_delete-simple-post"),
    # filter
    url(r'^filter/$',
        views.filter_simple_posts,
        name="testapp_filter-simple-post"),
    # clear
    url(r'^clear/$',
        views.delete_all_simple_posts,
        name="testapp_clear-simple-post"),

    # ===================================
    # Forms
    # ===================================
    # create
    url(r'^create-simple-post-form/create/$',
        views.simple_post_form,
        name="testapp_create-simple-post-form"),

    # ===================================
    # Class-based View
    # ===================================
    # create
    url(r'^create-simple-post-from-class/create/$',
        views.SimplePostView.as_view(),
        name="testapp_create-simple-post-form-class"),
]

