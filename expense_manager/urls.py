from django.urls import path, reverse_lazy, re_path, include

# project
from .views import dashboard, uploadImage
from .resources import ExpenseResource, BudgetResource

from tastypie.api import Api 
v1_api = Api(api_name='v1')
v1_api.register(ExpenseResource())
v1_api.register(BudgetResource())

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('image/uploader/', uploadImage, name="image_uploader"),
    re_path(r'^api/', include(v1_api.urls)),
]