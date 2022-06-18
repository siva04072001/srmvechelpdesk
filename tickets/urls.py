from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('superadmin/', views.superadmin, name='superadmin'),
    path('superadminview/', views.superadminview, name='superadminview'),
    path('update_user/<int:Id>/', views.update_user, name='update_user'),
    path('delete_user/<int:Id>/', views.delete_user, name='delete_user'),
    path('assign_user/<int:Id>/', views.assign_user, name='assign_user'),
    path('engreport/<int:Id>/', views.engreport, name='engreport'),
    path('empreport/<int:Id>/', views.empreport, name='empreport'),
    path('adminreport/<int:Id>/', views.adminreport, name='adminreport'),
    path('adminHelpdesk/', views.admin, name='admin'),
    path('admintable/', views.admintable, name='admintable'),
    path('stats/', views.stats, name='stats'),
    path('adminclosed/', views.adminclosed, name='adminclosed'),
    path('adminprofile/', views.adminprofile, name='admin_profile'),
    path('empdetail/', views.userdetail, name='user_detail'),
    path('close_ticket/<int:Id>/', views.close_ticket, name='close_ticket'),
    path('assign_ticket/<int:Id>/', views.assign_ticket, name='assign_ticket'),
    path('update_ticket/<int:Id>/', views.update_ticket, name='update_ticket'),
    path('engassign_ticket/<int:Id>/', views.engassign_ticket, name='engassign_ticket'),
    path('engdetail_ticket/<int:Id>/', views.engdetail_ticket, name='engdetail_ticket'),
    path('engupdate_ticket/<int:Id>/', views.engupdate_ticket, name='engupdate_ticket'),
    path('engineer/', views.engineerticket, name='engineer'),
    path('engineerclosed/', views.engineerticketclosed, name='engineerclosed'),
    path('engineerdash/', views.engineerdash, name='engineerdash'),
    path('employee/', views.userticket, name='employee'),
    path('employee_status/', views.statusticket, name='employee_status'),
    path('empdetail_ticket/<int:Id>/', views.empdetail_ticket, name='empdetail_ticket'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)