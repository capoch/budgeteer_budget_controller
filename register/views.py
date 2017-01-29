from django.contrib import messages
from django.db.models import Sum
from django.http import HttpResponse, HttpResponseRedirect
from django_pandas.io import read_frame
from django.shortcuts import render, get_object_or_404, redirect, render_to_response

from .forms import EntryForm, CategoryForm
from .models import Entry

import numpy as np
from chartit import PivotDataPool, PivotChart


# Create your views here.
def registerEntry(request):
    form = EntryForm(request.POST or None)
    if form.is_valid():
        entry = form.save(commit=False)
        entry.amount_out = entry.amount / 50
        entry.save()
        messages.success(request,"Successfully created")
        return HttpResponseRedirect(entry.get_absolute_url())
    context = {
        "form":form,
    }
    return render(request,'form.html',context)

def detailEntry(request, pk):
    entry = get_object_or_404(Entry,pk=pk)
    context = {
        "entry" : entry,
    }
    print(context)
    return render(request,'detail.html', context)

def listEntry(request):
    queryset = Entry.objects.all()
    context = {
    "entrylist" : queryset,
    }
    print(context)
    return render(request, 'list.html', context)

def overviewEntry(request):
    queryset = Entry.objects.all()
    df = read_frame(queryset)
    cols='category'
    rows='date'
    # if 'curr'=='CHF':
    #     values='amount_out'
    # if 'curr'=='PHP':
    values='amount'
    search_from = request.GET.get('d_from')
    search_to = request.GET.get('d_to')
    curr = request.GET.get('curr')
    if curr=='CHF':
        values='amount_out'
    if search_from:
        queryset = queryset.filter(date__gte=search_from)
    if search_to:
        queryset = queryset.filter(date__lte=search_to)
    pt = queryset.to_pivot_table(values=values, rows=rows, cols=cols, aggfunc=np.sum, margins=True, dropna=True).fillna(value=0)
    pt=pt.to_html()
    context={
    "data":pt,
    }
    return render(request, 'overview.html', context)

def categoryView(request):
    cat = request.GET.get('cat')
    queryset = Entry.objects.filter(category__category_name=cat)
    cols='category'
    rows='date'
    values='amount'
    pt = queryset.to_pivot_table(values=values, rows=rows, cols=cols, aggfunc=np.sum, margins=True, dropna=True).fillna(value=0)
    pt=pt.to_html()
    context={
    "data":pt,
    }
    return render(request, 'cat_view.html', context)

def dateView(request, *args, **kwargs):
    return HttpResponse("Date page")

def addCategory(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        entry = form.save(commit=False)
        entry.save()
        messages.success(request,"Successfully created")
        return redirect('register')
    context = {
        "form":form,
    }
    return render(request,'add_cat.html',context)




def entry_pivot_chart_view(request):
# Step 1: Create a PivotDataPool with the data we want to retrieve.
    entrypivotdata = PivotDataPool(
    series=[{
    'options': {
    'source': Entry.objects.all(),
    'categories': ['date'],
    'legend_by': 'category',
    },
    'terms': {
    'sum_amount': Sum('amount'),
    }
    }]
    )
    # Step 2: Create the PivotChart object
    rainpivcht = PivotChart(
    datasource=entrypivotdata,
    series_options=[{
    'options': {
    'type': 'column',
    'stacking': True
    },
    'terms': ['sum_amount']
    }],
    chart_options={
    'title': {
    'text': 'Ausgaben per Datum und Kategorie'
    },
    'xAxis': {
    'title': {
    'text': 'Month'
    }
    }
    }
    )
    # Step 3: Send the PivotChart object to the template.
    return render(request,'graph.html',{'rainpivchart': rainpivcht,})
