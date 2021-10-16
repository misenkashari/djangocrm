from os import replace
from django.shortcuts import redirect, render
from .models import Csv
from users.models import User
from leads.models import Lead
from sources.models import Source
from categories.models import Category
from .forms import CsvForm
import csv

# Create your views here.

def upload_file(request):
    all_data = []
    form = CsvForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)

            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    name = row[0].upper()
                    source = Source.objects.get(source=row[1])
                    user = User.objects.get(username=row[2])
                    category = Category.objects.get(category=row[3])
                    phone = row[4].upper()
                    mail = row[5]
                    all_data.append(Lead(name=name, source=source, user=user, category=category, phone=phone, email=mail))
                obj.activated = True
                obj.save()
        Lead.objects.bulk_create(all_data)
        return redirect("leads:lead-index")

    return render(request, 'csvs/index.html', {'form': form, })
