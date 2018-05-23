from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotFound


# ===================================
# Response, Context, Template
# ===================================

# View 1: HttpResponse
from django.views import View


def view_http_response(request):
    html_string = "<html><body><h1>Header 1</h1><p>Text 1</p></body></html>"
    return HttpResponse(html_string)


# View 2: HttpResponse with variables
def view_http_response_with_var(request):
    header = "Header 2"
    content = "Text 2"
    html_string = "<html><body><h1>%s</h1><p>%s</p></body></html>" % (header, content)
    return HttpResponse(html_string)


# View 3: HttpResponse with a template
from django.template import loader

def view_http_response_with_template(request):

    template = loader.get_template("simple_post_ui_app/templates/html_response_with_template.html")

    return HttpResponse(template.render())


# View 4: HttpResponse with a template and variables
def view_http_response_with_template_var(request):

    # comment: add the "./" path to the template DIRS in the settings.py
    template = loader.get_template("simple_post_ui_app/templates/html_response_with_template_var.html")

    context_var = {"header": "Header 4",
                   "content": "Text 4"}

    return HttpResponse(template.render(context_var, request))


from django.shortcuts import render, redirect


# View 5: HttpResponse with a template and variables. Approach 2 (main)
def view_http_response_with_template_var_2(request):

    context_var = {"header": "Header 5",
                   "content": "Text 5"}

    return render(request, "simple_post_ui_app/templates/html_response_with_template_var.html", context_var)


# View 6: HttpResponseRedirect
from django.urls import reverse


def view_http_redirect(request):
    return HttpResponseRedirect("http://mail.ru", permanent=False) #True - HTTP Response Code 301; False - 302
    #return HttpResponseRedirect("/simple_post_ui_app/view-http-response/")
    #return HttpResponseRedirect(reverse("testapp_view-http-response"))
    #return redirect("testapp_view-http-response")

# View 7: JsonResponse
def view_json_response(request):

    data = {"header": "Header 7",
            "content": "Text 7"}

    return JsonResponse(data)


# ===================================
# Template with static files
# ===================================

# View 8:
def view_http_response_with_static(request):
    #print(STATIC_ROOT)
    context_var = {"header": "Header 5",
                   "content": "Text 5"}

    return render(request, "simple_post_ui_app/templates/html_response_with_static.html", context_var)


# ===================================
# Parameters - URL, GET, POST
# ===================================

# 9. View Args
def view_http_response_url_args(request, *args):

    header = "Default Header"
    content = "Default Content"

    if len(args) > 0:
        header = args[0]
    if len(args) > 1:
        content = args[1]

    context_var = {"header": header,
                   "content": content}

    return render(request, "simple_post_ui_app/templates/html_response_with_template_var.html", context_var)


# 10. View Kwargs
def view_http_response_url_kwargs(request, header="Default Header", content="Default Content"):

    context_var = {"header": header,
                   "content": content}

    return render(request, "simple_post_ui_app/templates/html_response_with_template_var.html", context_var)


# 11. View GET and POST
def view_http_response_get_post(request):

    context_var = {"header": None,
                   "content": None}

    if request.method == "GET":
        context_var["header"] = request.GET.get("header", None)
        context_var["content"] = request.GET.get("content", None)

    if request.method == "POST":
        context_var["header"] = request.POST.get("header", None)
        context_var["content"] = request.POST.get("content", None)

    if context_var["header"] is None and context_var["content"] is None:
        return render(request, "simple_post_ui_app/templates/html_response_get_post.html", context_var)

    return render(request, "simple_post_ui_app/templates/html_response_get_post_content.html", context_var)


# ===================================
# Models
# ===================================
from simple_post_ui_app.models import SimplePost


# create
def create_simple_post(request):

    if request.method == "POST":

        header = request.POST.get("header", None)
        content = request.POST.get("content", None)

        if header is not None and content is not None:
            #obj = SimplePost.objects.create(header=header, content=content) # in one step
            obj = SimplePost(header=header, content=content)
            obj.save()
            return redirect("testapp_simple-post-list")

    if request.method == "GET":
        return render(request, "simple_post_ui_app/templates/simple_post_create.html")

    return HttpResponseNotFound("<h1>Unable to perform</h1>")


# select
def simple_post_list_view(request, pk=None):

    if request.method == "GET" and pk is None:
        objs = SimplePost.objects.all()
        context_var = {"simple_post_objects": objs}
        return render(request, "simple_post_ui_app/templates/simple_post_list.html", context_var)

    if request.method == "GET" and pk is not None:
        obj = SimplePost.objects.get(id=pk)
        context_var = {"simple_post_object": obj}
        return render(request, "simple_post_ui_app/templates/simple_post_detail.html", context_var)

    return HttpResponseNotFound("<h1>Unable to perform</h1>")


# update
def update_simple_post(request, pk=None):

    if request.method == "POST":

        id = request.POST.get("id", None)
        header = request.POST.get("header", None)
        content = request.POST.get("content", None)

        if header is not None and content is not None and id is not None:
            try:
                obj = SimplePost.objects.get(pk=id)
                obj.header = header
                obj.content = content
                obj.save(update_fields=["header", "content", "updated"])
            except SimplePost.DoesNotExist:
                raise Http404("There is no such id")

            return redirect("testapp_simple-post-list")

    return HttpResponseNotFound("<h1>Unable to perform</h1>")


# delete
def delete_simple_post(request, pk=None):

    if request.method == "POST":

        id = request.POST.get("id", None)

        if id is not None:
            try:
                obj = SimplePost.objects.get(pk=id)
                obj.delete()
            except SimplePost.DoesNotExist:
                raise Http404("There is no such id")

            return redirect("testapp_simple-post-list")

    return HttpResponseNotFound("<h1>Unable to perform</h1>")


# clear
def delete_all_simple_posts(request):
    if request.method == "POST":
        SimplePost.objects.all().delete()
        return redirect("testapp_simple-post-list")

    return HttpResponseNotFound("<h1>Unable to perform</h1>")


# filter
def filter_simple_posts(request):

    key_word = request.GET.get("keyword", "")

    objs = SimplePost.objects.filter(header__icontains=key_word)
    context_var = {"simple_post_objects": objs}

    return render(request, "simple_post_ui_app/templates/simple_post_list.html", context_var)


# ===================================
# Forms
# ===================================
from simple_post_ui_app.forms import SimplePostForm, SimplePostModelForm


def simple_post_form(request):

    if request.method == "POST":
        form = SimplePostForm(request.POST)
        if form.is_valid():
            SimplePost.objects.create(header=form.cleaned_data["header"], content=form.cleaned_data["content"])
            return redirect("testapp_simple-post-list")

    if request.method == "GET":
        form = SimplePostForm()
        return render(request, "simple_post_ui_app/templates/simple_post_create_with_form.html", {'form': form})


# ===================================
# Class-based View
# ===================================
class SimplePostView(View):

    def get(self, request):
        form = SimplePostModelForm()
        return render(request, "simple_post_ui_app/templates/simple_post_create_with_form_class.html", {'form': form})

    def post(self, request):

        form = SimplePostModelForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("testapp_simple-post-list")

        return render(request, "simple_post_ui_app/templates/simple_post_create_with_form_class.html", {'form': form})