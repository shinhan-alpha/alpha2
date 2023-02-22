from django.contrib import admin
from .models import Portfolio, Dividend

# Register your models here.
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    pass

@admin.register(Dividend)
class PortfolioAdmin(admin.ModelAdmin):
    pass