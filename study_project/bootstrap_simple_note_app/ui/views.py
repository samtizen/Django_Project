from django.contrib.auth import authenticate, login, REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from bootstrap_simple_note_app.models import SimpleNote
from bootstrap_simple_note_app.ui.forms import CustomAuthenticationForm, SimpleNoteForm, CustomSignUpForm, UserProfileForm


# ==========================================
# USER ACCOUNT
# ==========================================

class SimpleNoteLoginView(LoginView):

    template_name = "bootstrap_login.html"
    authentication_form = CustomAuthenticationForm

    def get_success_url(self):
        url = self.request.POST.get(REDIRECT_FIELD_NAME, None)
        return url or reverse_lazy("bootstrap-note:list")


class SimpleNoteLogoutView(LogoutView):
    next_page = reverse_lazy("bootstrap-note:list")


class SimpleNoteSignUpView(CreateView):

    form_class = CustomSignUpForm
    template_name = "bootstrap_register.html"
    success_url = reverse_lazy("bootstrap-note:list")

    def form_valid(self, form):

        self.object = form.save()

        new_user = authenticate(username=self.object.username, password=form.cleaned_data["password1"],)
        login(self.request, new_user)

        return redirect(self.get_success_url())


class SimpleNoteUserProfile(UpdateView):

    model = User
    form_class = UserProfileForm
    template_name = "bootstrap_note_profile.html"
    success_url = reverse_lazy("bootstrap-note:list")

    def get_object(self, queryset=None):
        return self.request.user


# ==========================================
# SIMPLE POST
# ==========================================

# List of posts
class SimpleNoteListView(ListView):

    model = SimpleNote
    template_name = "bootstrap_note_list.html"
    ordering = ["-created"]

    def get_queryset(self):

        keyword = self.request.GET.get("keyword", None)

        queryset = super().get_queryset()

        if keyword is not None:
            queryset = queryset.filter(header__icontains=keyword)

        return queryset


# List of posts
@method_decorator(login_required(login_url=reverse_lazy("bootstrap-note:login")), name="dispatch")
class SimpleNoteUserListView(ListView):

    model = SimpleNote
    template_name = "bootstrap_note_user_list.html"

    def get_queryset(self):

        queryset = super().get_queryset()

        return queryset.filter(user=self.request.user).order_by("-created")


# Create a new post
@method_decorator(login_required(login_url=reverse_lazy("bootstrap-note:login")), name="dispatch")
class SimpleNoteCreateView(CreateView):

    form_class = SimpleNoteForm
    template_name = "bootstrap_note_create.html"
    success_url = reverse_lazy("bootstrap-note:user-list")

    def form_valid(self, form):

        obj = form.save(commit=False)
        obj.user = self.request.user
        return super().form_valid(form)


# Update a post
@method_decorator(login_required, name="dispatch")
class SimpleNoteUpdateView(UpdateView):

    model = SimpleNote
    form_class = SimpleNoteForm
    template_name = "bootstrap_note_update.html"
    success_url = reverse_lazy("bootstrap-note:user-list")

    def get_object(self, queryset=None):

        pk = self.kwargs.get("pk")

        if pk is not None:
            try:
                return self.model.objects.get(pk=pk, user=self.request.user)
            except self.model.DoesNotExist:
                raise Http404

        raise Http404


# Delete a post
@method_decorator(login_required, name="dispatch")
class SimpleNoteDeleteView(DeleteView):

    model = SimpleNote
    success_url = reverse_lazy("bootstrap-post:list")
    template_name = "bootstrap_note_delete.html"

    def get_object(self, queryset=None):

        obj = super().get_object()
        if obj.user == self.request.user:
            return obj

        raise Http404()

"""class SimpleNoteView(View):
    def get(self, request):
        pass
    def post(self, request):
        pass

"""