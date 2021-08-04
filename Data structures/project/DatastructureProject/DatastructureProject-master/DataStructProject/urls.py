"""DataStructProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from classRoomCheck import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.information,name='UserContact'),
    path('register/',views.registerPage),
    path('userInformation/',views.userInformation),
    path('userLink/<str:name>',views.userLink),
    path('classStatus/searchInAllStudent',views.searchInAllStudent),
    path('register/addFormedRegister',views.addFormedRegister),
    path('registerAsTeach/',views.registerPageAsTeach),
    path('registerAsTeach/addFormedRegisterAsTeach',views.addFormedRegisterAsTeach),
    path('classStatus/',views.allStudentName,name='ClassStatus'),
    path('dataStructlogin/',views.dataStructlogin,name='DataStructMember'),
    path('dataStructlogin/dataStructStart',views.dataStructStart),
    path('comNetlogin/',views.comNetlogin,name='ComnetMember'),
    path('comNetlogin/comNetStart',views.comNetStart),
    path('comOrglogin/',views.comOrglogin,name='ComOrgMember'),
    path('comOrglogin/comOrgStart',views.comOrgStart),
    path('epplogin/',views.ePPlogin,name='EppMember'),
    path('epplogin/eppStart',views.ePPStart),
    path('problogin/',views.problogin,name='Probmember'),
    path('problogin/probStart',views.probStart),
    path('dataStructlogin/addIDNameDatastruct',views.dataStructloginAddIDandName),
    path('dataStructlogin/dataStructlogout/<str:fullName>',views.dataStructlogoutlink),
    path('dataStructlogin/dataStructlogout',views.dataStructlogout),
    path('dataStructlogin/dataEndClass',views.dataEndClass),
    path('comNetlogin/addIDNameComNet',views.comNetloginAddIDandName),
    path('comNetlogin/comNetlogout/<str:fullName>',views.comNetlogoutlink),
    path('comNetlogin/comNetlogout',views.comNetlogout),
    path('comNetlogin/comNetEndClass',views.comNetEndClass),
    path('comOrglogin/addIDNameComOrg',views.comOrgloginAddIDandName),
    path('comOrglogin/comOrglogout/<str:fullName>',views.comOrglogoutlink),
    path('comOrglogin/comOrglogout',views.comOrglogout),
    path('comOrglogin/comOrgEndClass',views.comOrgEndClass),
    path('epplogin/addIDNameEpp',views.ePPloginAddIDandName),
    path('epplogin/ePPlogout/<str:fullName>',views.ePPlogoutlink),
    path('epplogin/ePPlogout',views.ePPlogout),
    path('epplogin/ePPEndClass',views.ePPEndClass),
    path('problogin/addIDNameProb',views.probloginAddIDandName),
    path('problogin/problogout/<str:fullName>',views.problogoutlink),
    path('problogin/problogout',views.problogout),
    path('problogin/probEndClass',views.probEndClass),
    path('test/', views.test),
    path('loginGet', views.loginForm),
    path('', views.getStart),
    path('login', views.login),
    path('logout', views.logout),
    path('dataStructlogin/dataMinMaxID',views.dataMinMaxID),
    path('dataStructlogin/dataMaxMinID',views.dataMaxMinID),
    path('dataStructlogin/dataMinMaxDay',views.dataMinMaxDay),
    path('dataStructlogin/dataMaxMinDay',views.dataMaxMinDay),
    path('comNetlogin/comNetMinMaxID',views.comNetMinMaxID),
    path('comNetlogin/comNetMaxMinID',views.comNetMaxMinID),
    path('comNetlogin/comNetMinMaxDay',views.comNetMinMaxDay),
    path('comNetlogin/comNetMaxMinDay',views.comNetMaxMinDay),
    path('comOrglogin/comOrgMinMaxID',views.comOrgMinMaxID),
    path('comOrglogin/comOrgMaxMinID',views.comOrgMaxMinID),
    path('comOrglogin/comOrgMinMaxDay',views.comOrgMinMaxDay),
    path('comOrglogin/comOrgMaxMinDay',views.comOrgMaxMinDay),
    path('epplogin/ePPMaxMinDay',views.ePPMaxMinDay),
    path('epplogin/ePPMinMaxID',views.ePPMinMaxID),
    path('epplogin/ePPMaxMinID',views.ePPMaxMinID),
    path('epplogin/ePPMinMaxDay',views.ePPMinMaxDay),
    path('epplogin/ePPMaxMinDay',views.ePPMaxMinDay),
    path('epplogin/ePPMaxMinDay',views.ePPMaxMinDay),
    path('problogin/probMinMaxID',views.probMinMaxID),
    path('problogin/probMaxMinID',views.probMaxMinID),
    path('problogin/probMinMaxDay',views.probMinMaxDay),
    path('problogin/probMaxMinDay',views.probMaxMinDay),
    path('aboutus', views.aboutus),
    path('dataDetail', views.dataStructDetail),
    path('netDetail', views.comNetDetail),
    path('orgDetail', views.comOrgDetail),
    path('eppDetail', views.eppDetail),
    path('probDetail', views.probDetail),
    path('test001/',views.test001)
]

urlpatterns += staticfiles_urlpatterns()