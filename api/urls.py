
from django.urls import path, include
from .views import ArticleViewset, UserViewset, CommentViewset
from rest_framework.routers import DefaultRouter

#from .views import ArticleList, ArticleDetail

router = DefaultRouter()
router.register('articles', ArticleViewset, basename='articles')
router.register('comments', CommentViewset, basename='comments')
router.register('users', UserViewset)


urlpatterns = [
    
    path('api/', include(router.urls)),
    
   # path('articles/', ArticleList.as_view()),
   # path('articles/<int:id>/', ArticleDetail.as_view()),

    #path('articles/', article_list, name='article_list'),
    #path('articles/<int:pk>/', article_details )
]