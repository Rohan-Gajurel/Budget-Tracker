from django.urls import path
from budget_tracker_app import views

urlpatterns = [
    path('', views.transaction_list, name="list-transactions"),
    path('delete/<int:id>/', views.delete_transaction, name="transaction-delete"),
    path('create/', views.create_transaction, name="create-transaction"),
    path("filter/", views.filter_transaction, name="filter-transaction"),
]