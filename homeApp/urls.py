from django.contrib import admin
from django.urls import path
from homeApp import views

urlpatterns = [
    path('',views.admin_login,name='login'), # agar blank path leke ata hai jo views kay index function per bhejdo jiska naam Home hai 
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
 
  #  path('login/', views.admin_login, name='login'),  # Login page route
    #path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard route
  #  path('payment',views.payment,name='payment'),
    path('dashboard/', views.dashboard, name='dashboard'),
  #  path('chatbot/', views.chatbot_view, name='chatbot'),
    
    path('personal_info',views.personal_info,name='personal_info'),
    path('contact_dev',views.contact_dev,name='contact_dev'),

    path('logout/', views.logout_view, name='logout'),
    path('payment/', views.payment_page, name='payment_page'),
    path('process-payment/', views.process_payment, name='process_payment'),  # For handling payment actions

    path('graphs-page/', views.graphs_page, name='graphs-page'),
 #   path('dashboard/add_member',views.add_member,name='add_member'),
 #    path('dashboard/view_members', views.view_members, name='view_members'),

 #   path('edit_member/<int:member_id>/', views.edit_member, name='edit_member'),
 #   path('delete_member/<int:member_id>/', views.delete_member, name='delete_member'),



   path('dashboard/view_members/', views.view_members, name='view_members'),  # Add this line
   path('dashboard/add_member/', views.add_member, name='add_member'),
   path('dashboard/edit_member/<int:member_id>/', views.edit_member, name='edit_member'),
   path('dashboard/delete_member/<int:member_id>/', views.delete_member, name='delete_member'),

   path('dashboard/assign_membership/', views.assign_membership, name='assign_membership'),
  #  path('dashboard/view_memberships/', views.view_memberships, name='view_memberships'),  # Add this line
  #  path('dashboard/edit_membership/<int:membership_id>/', views.edit_membership, name='edit_membership'),
  #  path('dashboard/delete_membership/<int:membership_id>/', views.delete_membership, name='delete_membership'),
   
# URLs for Memberships
path('dashboard/view_memberships/', views.view_memberships, name='view_memberships'),
path('dashboard/edit_membership/<int:membership_id>/', views.edit_membership, name='edit_membership'),
path('dashboard/delete_membership/<int:membership_id>/', views.delete_membership, name='delete_membership'),


   path('dashboard/add_trainer/', views.add_trainer, name='add_trainer'),
   path('dashboard/view_trainer/', views.view_trainers, name='view_trainers'),
   path('edit_trainer/<int:trainer_id>/', views.edit_trainer, name='edit_trainer'),
   path('delete_trainer/<int:trainer_id>/', views.delete_trainer, name='delete_trainer'),
   path('dashboard/assign_trainer/', views.assign_trainer, name='assign_trainer'),
   path('dashboard/view_trainer_assignments/', views.view_trainer_assignments, name='view_trainer_assignments'),

   path('dashboard/view_plans/', views.view_plans, name='view_plans'),
   path('dashboard/add_plan/', views.add_plan, name='add_plan'),
   path('dashboard/edit_plan/<int:plan_id>/', views.edit_plan, name='edit_plan'),
   path('dashboard/delete_plan/<int:plan_id>/', views.delete_plan, name='delete_plan'),




]  