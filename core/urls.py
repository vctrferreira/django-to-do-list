from django.conf.urls import url
from core.views import TodoListView


urlpatterns = [
    url(r'^list/', TodoListView.as_view(), name="core.create_new_todo"),
    url(r'^update/', TodoListView.as_view(), name="core.edit_todo"),    
]
