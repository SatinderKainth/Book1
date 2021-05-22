from django.urls import path
from . import views

urlpatterns =[
    path('',views.index),
    path('add-book',views.add_book),
    path('add-author',views.add_author),
    path('books/<int:book_id>',views.edit_book),
    path('book-to-author/<int:book_id>',views.book_to_author),
    path('authors/<int:author_id>',views.author_edit),
    path('author-to-book/<int:author_id>',views.author_to_book),
]