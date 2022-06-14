from django.urls import path
from . import views


urlpatterns = [
    path('empview/', views.emp_View, name='empview_url'),
    path('showemp/', views.Showemp_View, name='showempinfo_url'),
    path('uemp/<int:id>/', views.Update_View, name='update_url'),
    path('delemp/<int:id>/', views.Delete_View, name='delete_url'),
    #path('pdf/<int:pk>/',views.perticularData, name='pdf2_url'),
    #path('pdf/',views.GenaratePDF, name='pdf_url'),
]