from .models import Lead
import django_filters
import flatpickr


class LeadFilter(django_filters.FilterSet):

    class Meta:
        model = Lead
        
        fields = {
         'name': ['icontains', ],
         'phone': ['icontains', ],
         'source':['exact',] ,
         'created_at': ['date', 'date__gt', 'date__lt',],
         'category': ['exact', ],
         'user': ['exact', ],
         'task': ['date'],
        }


    widgets = {
         'created_at__date': flatpickr.DateTimePickerInput(attrs={'placeholder':'Select Date/Time.'}),
         'created_at__date__gt': flatpickr.DateTimePickerInput(attrs={'placeholder':'Select Date/Time.'}),
         'created_at__date__lt': flatpickr.DateTimePickerInput(attrs={'placeholder':'Select Date/Time.'}),
      }
