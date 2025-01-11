from django.contrib.gis.db import models

class planning_case(models.Model):
    case_number = models.CharField(max_length=30, blank=False, unique=True)
    case_date = models.DateField(blank=False)

    case_type = models.CharField(max_length=200, blank=True)
    location = models.TextField(max_length=1024, blank=True)
    description = models.TextField(max_length=1024, blank=True)
    owner = models.CharField(max_length=1024, blank=True)

    case_url = models.URLField(blank=True)
    geometry_pnt = models.PointField(blank=True, null=True)
    geometry_poly = models.PolygonField(blank=True, null=True)

    parcel_number = models.CharField(max_length=20, blank=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.case_number

class area_of_interest(models.Model):
    geometry = models.PolygonField()
    name = models.CharField(max_length=200, blank=False)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
