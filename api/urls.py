from rest_framework.routers import DefaultRouter
from .views import PostList

app_name = 'api'


router = DefaultRouter()
router.register('posts', PostList, basename='post')
urlpatterns = router.urls

# urlpatterns = [
#    path('<int:pk>/', PostDetail.as_view(), name="detailcreate"), #pk - primary key(ключевое поле)
#    path('', PostList.as_view(), name="listcreate"),
# ]
