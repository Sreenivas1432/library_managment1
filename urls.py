from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from management import views
from .feed import LatestEntriesFeed

urlpatterns = &  # 91;
path('admin/', admin.site.urls),
path('', views.index, name='index'),

path('books/', views.BookListView, name='books'),
path('book/&lt;int:pk&gt;', views.BookDetailView, name='book-detail'),
path('book/create/', views.BookCreate, name='book_create'),
path('book/&lt;int:pk&gt;/update/', views.BookUpdate, name='book_update'),
path('book/&lt;int:pk&gt;/delete/', views.BookDelete, name='book_delete'),

path('student/&lt;int:pk&gt;/delete/', views.StudentDelete, name='student_delete'),
path('student/create/', views.StudentCreate, name='student_create'),
path('student&lt;int:pk&gt;/update/', views.StudentUpdate, name='student_update'),
path('student/&lt;int:pk&gt;', views.StudentDetail, name='student_detail'),
path('student/', views.StudentList, name='student_list'),
path('student/book_list', views.student_BookListView, name='book_student'),
path('book/&lt;int:pk&gt;/request_issue/', views.student_request_issue, name='request_issue'),

path('feed/', LatestEntriesFeed(), name='feed'),
path('return/&lt;int:pk&gt;', views.ret, name='ret'),
path('rating/&lt;int:pk&gt;/update/', views.RatingUpdate, name='rating_update'),
path('rating/&lt;int:pk&gt;/delete/', views.RatingDelete, name='rating_delete'),

url(r'^search_b/', views.search_book, name="search_b"),
url(r'^search_s/', views.search_student, name="search_s")
]
urlpatterns += &  # 91;
path('accounts/', include('django.contrib.auth.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
