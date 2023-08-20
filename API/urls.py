from django.urls import path, include

from . import views

app_name = "API"

manufacturer_list_create = views.ManufacturerViewSet.as_view(
    {"get": "list", "post": "create"}
)
manufacturer_detail = views.ManufacturerViewSet.as_view(
    {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
)


manufacturer_url = [
    path("", manufacturer_list_create),
    path("<int:pk>/", manufacturer_detail),
]

urlpatterns = [
    path("manufacturer/", include(manufacturer_url)),
    # path("series/", include(cliente_url)),
    # path("product/", include(cliente_url)),
]
