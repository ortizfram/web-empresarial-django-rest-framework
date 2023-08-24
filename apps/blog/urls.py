# blog app urls.py
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import *

urlpatterns = [
    path('', BlogListView.as_view()),
    path('category/<category_id>', BlogListCategoryView.as_view()),
    path('<post_slug>', PostDetailView.as_view()),
    path('search/<str:search_term>', SearchBlogView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
