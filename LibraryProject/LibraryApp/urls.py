from django.urls import path

from LibraryApp import views

urlpatterns=[
    path('', views.log_fun, name='log'),
    path('logindata', views.logdata_fun),
    path('regadm', views.regadm_fun, name='adreg'),
    path('read', views.read_fun),
    path('regstu', views.regstu_fun,name='streg'),
    path('readdata', views.readdata_fun),
    path('adminhome', views.adhome_fun, name='adhome'),
    path('studenthome', views.sthome_fun, name='sthome'),
    path('add_book', views.add_book_fun, name='add'),
    path('adddata', views.adddata_fun),
    path('display', views.display_fun, name='display'),  # it will display student table data in display.html file
    path('update/<int:id>', views.update_fun, name='update'),  # it will update the student data
    path('delete/<int:id>', views.delete_fun, name='del'),  # it will delete the record from student table

    path('assi', views.assi_fun, name='assi'),
    path('assign',views.assign_fun),
    path('readassi',views.readassign_fun),


    # path('issue',views.issue_fun,name='issue'),
    path('issue', views.display1_fun, name='issue'),

    path('updt/<int:id>', views.update1_fun, name='upda'),
    path('dele/<int:id>', views.delete1_fun, name='delete'),

    path('issue1', views.issue1_fun,name='issue1'),
    path('log_out', views.log_out_fun, name='log_out'),

]