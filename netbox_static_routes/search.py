"""Global search register for static_routes by andyb2000."""

from netbox.search import SearchIndex, register_search
from .models import StaticRoute

@register_search
class StaticRouteIndex(SearchIndex):
    model = StaticRoute
    fields = (
        ('destination_prefix', 100),
        ('next_hop', 100),
    )

