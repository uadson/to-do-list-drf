# from django.urls import path

# from core.views.home_view import TodoListAndCreate, TodoDetailChangeAndDelete

# from core.views.home_view import todo_list, todo_detail_change_and_delete

from core.views.home_view import TodoViewSet

from rest_framework.routers import DefaultRouter


app_name = 'core'

router = DefaultRouter()
router.register(r'', TodoViewSet)
urlpatterns = router.urls

# urlpatterns = [
#    with Class Based View
#
#    path('', TodoListAndCreate.as_view(), name='todo_list'),
#    path('<int:pk>/', TodoDetailChangeAndDelete.as_view(), name='detail_change_delete'),
#
#    with Function Based View
#
#    path('', todo_list, name='todo_list'),
#    path('<int:pk>/', todo_detail_change_and_delete, name='detail_change_delete'),
# ]
