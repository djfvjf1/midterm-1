from django.urls import path

from . import views

urlpatterns = [

    

    path('', views.prehome, name='prehome'),
    path('home/', views.home, name='home'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/', views.profile_view, name='profile'),

    path('table/', views.new_form, name='create_table'),
    path('table/<int:pk>/', views.table_page, name = 'table_page'),
    path('table23/', views.new_form23, name='create_table23'),
    path('table23/<int:pk>/', views.table_page23, name = 'table_page23'),
    path('table26/', views.new_form26, name='create_table26'),
    path('table26/<int:pk>/', views.table_page26, name = 'table_page26'),  

    path('export/', views.export_data_to_word, name='export_data_to_word')
]