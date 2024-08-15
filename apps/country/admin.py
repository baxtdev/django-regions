from django.contrib import admin

from .models import Country,Region,City

class RegionInline(admin.TabularInline):
    model = Region
    extra = 0
    show_change_link = True



class CityInline(admin.TabularInline):
    model = City
    extra = 0
    show_change_link = True
    show_full_result_count = True
    sortable_by = 'id'


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name',]
    ordering = ('name',)
    inlines = [RegionInline]



@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ['name', 'country__name']
    ordering = ('name',)
    inlines = [CityInline]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'region')
    search_fields = ['name','region__name']
    ordering = ('name',)
