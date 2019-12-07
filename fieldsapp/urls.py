from django.urls import path
from fieldsapp.views import BlogListView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),

]
