from django.shortcuts import render, reverse, redirect
from django.views import generic
from .forms import LeadModelForm, LeadModifyForm, CommentForm
from .models import Comment, Lead
from django.db.models import Q
from .filters import LeadFilter
from django_filters.views import FilterView, object_filter
from users.views import staff
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


class LeadCreateView(staff, generic.CreateView):
    model = Lead
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-index")


class LeadUpdateView(generic.UpdateView):
    model = Lead
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['commentform'] = CommentForm()
        return context

    def get_success_url(self):
        return reverse("leads:lead-index")


class LeadIndexView(generic.ListView):
    model = Lead
    ordering = ['-updated_at']
    template_name = 'leads/lead_index.html'
    paginate_by = 100

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['form'] = LeadModifyForm()
        return context


def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    if request.user.is_superuser:
        lead.delete()
    else:
        raise PermissionDenied("Access forbidden 403. Are you root?")
    return redirect("/leads")


class LeadView(staff, generic.View):
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            lead_ids = request.POST.getlist('id[]')
            for id in lead_ids:
                lead = Lead.objects.get(pk=id)
                lead.delete()
            return redirect("/leads")


class ModifyView(staff, generic.View):
    def post(self, request):
        lead_list = []
        if request.method == "POST":
            form = LeadModifyForm(request.POST)
            lead_ids = request.POST.getlist('id[]')
            for id in lead_ids:
                lead = Lead.objects.get(pk=id)
                if form.is_valid():
                    user = form.cleaned_data['user']
                    category = form.cleaned_data['category']
                    lead.user = user
                    lead.category = category
                lead_list.append(lead)
        Lead.objects.bulk_update(lead_list, ['category', 'user'])
        return redirect("leads:lead-index")


class SearchResultsView(generic.ListView):
    model = Lead
    template_name = 'leads/lead_index.html'
    paginate_by = 100
    ordering = ['-updated_at']

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['form'] = LeadModifyForm()
        return context

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        if query:
            q_list = Lead.objects.filter(
                Q(name__icontains=query) | Q(phone__icontains=query) | Q(id__icontains=query) |
                Q(email__icontains=query) | Q(category__category__icontains=query) |
                Q(source__source__icontains=query) | Q(created_at__icontains=query) | Q(
                    user__username__icontains=query) | Q(id__icontains=query) | Q(task__icontains=query)
            ).order_by('-updated_at')
            return q_list
        return Lead.objects.all().order_by('-updated_at')


class LeadAdvancedSearch(FilterView):
    paginate_by = 100
    filterset_class = LeadFilter
    template_name = 'leads/search_index.html'
    queryset = Lead.objects.all().order_by('-updated_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = LeadModifyForm()
        return context




class CommentView(generic.CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'leads/lead_comment.html'

    def form_valid(self, form):
        form.instance.lead_id = self.kwargs['pk']
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        pk = self.kwargs.get('pk')
        lead = Lead.objects.get(id=pk)
        return reverse("leads:lead-update", kwargs={'pk': lead.pk})
