from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import planning_case, area_of_interest


class PlanningCaseListView(ListView):
    model = planning_case

class AOIPlanningCaseListView(ListView):
    def get_queryset(self):
        self.aoi = get_object_or_404(area_of_interest, id=self.kwargs['id'])
        return planning_case.objects.filter(geometry_pnt__within=aoi.geometry)

class PlanningCaseDetailView(DetailView):
    model = planning_case
