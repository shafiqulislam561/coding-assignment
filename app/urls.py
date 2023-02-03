from django.urls import path

from app.views import ParentListView, ParentCreate, ParentUpdate, ParentDelete
from app.views import ChildListView, ChildCreate, ChildUpdate, ChildDelete

app_name = "app"

urlpatterns = [
    # Parent URLs
    path('parent/list', ParentListView.as_view(), name='parents'),
    path('parent/create', ParentCreate.as_view(), name='create.parent'),
    path('parent/update/<int:pk>', ParentUpdate.as_view(), name='update.parent'),
    path('parent/delete/<int:pk>', ParentDelete.as_view(), name='delete.parent'),

    # Child URLs
    path('child/list', ChildListView.as_view(), name='children'),
    path('child/create', ChildCreate.as_view(), name='create.child'),
    path('child/update/<int:pk>', ChildUpdate.as_view(), name='update.child'),
    path('child/delete/<int:pk>', ChildDelete.as_view(), name='delete.child'),
]