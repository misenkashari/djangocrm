from django.urls import path
from django.conf.urls import url
from .views import CommentView, LeadCreateView, LeadUpdateView, ModifyView, lead_delete, LeadView, LeadIndexView, SearchResultsView, LeadAdvancedSearch
from django.contrib.auth.decorators import login_required



app_name = "leads"
urlpatterns =[
    path('', login_required(LeadIndexView.as_view()), name='lead-index'),
    path('<int:pk>/update/', login_required(LeadUpdateView.as_view()), name='lead-update'),
    url(r'^create/$', login_required(LeadCreateView.as_view()), name='lead-create'),
    path('<int:pk>/delete/', login_required(lead_delete), name='lead-delete'),
    url(r'^delete/$', login_required(LeadView.as_view()), name='delete-multiple'),
    url(r'^modify/$', login_required(ModifyView.as_view()), name='modify'),
    url(r'^search/$', login_required(SearchResultsView.as_view()), name='search'),
    url(r'^filtering/$', login_required(LeadAdvancedSearch.as_view()), name='advanced-search'),
    path('<int:pk>/comment', (CommentView.as_view()), name='comment'),


    #path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead-update'),
    #path('create/', LeadCreateView.as_view(), name='lead-create'),
    #path('<int:pk>/delete/', lead_delete, name='lead-delete'),
    #path('delete/', LeadView.as_view(), name='delete-multiple'),
    #path('search/', SearchResultsView.as_view(), name='search'),
    #path('searching/', LeadAdvancedSearch.as_view(), name='advanced-search'),
    #path('status/', LeadAdvancedStatus.as_view(), name='status'),
]