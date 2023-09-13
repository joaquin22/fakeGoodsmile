from django.urls import path, include

from . import views

app_name = "API"

manufacturer_list_create = views.ManufacturerViewSet.as_view(
    {"get": "list", "post": "create"}
)
manufacturer_detail = views.ManufacturerViewSet.as_view(
    {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
)

serie_list_create = views.SerieViewSet.as_view({"get": "list", "post": "create"})

serie_detail = views.SerieViewSet.as_view(
    {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
)

product_list_create = views.ProductViewSet.as_view({"get": "list", "post": "create"})

product_detail = views.ProductViewSet.as_view(
    {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
)


manufacturer_url = [
    path("", manufacturer_list_create),
    path("<int:pk>/", manufacturer_detail),
]

serie_url = [
    path("", serie_list_create),
    path("<int:pk>/", serie_detail),
]

product_url = [
    path("", product_list_create),
    path("<int:pk>/", product_detail),
]


auth_url = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("register/", views.RegisterView.as_view(), name="register"),
]

urlpatterns = [
    path("manufacturer/", include(manufacturer_url)),
    path("serie/", include(serie_url)),
    path("product/", include(product_url)),
    path("auth/", include(auth_url)),
]
