from django.urls import path, re_path
from app import views, mobileViews

urlpatterns = [
    re_path(r'^.*\.html', views.gentella_html, name='gentella'),
    path('', views.index, name='index'),
    # -------------------------------------------------------------------------------
    # cordova
    # mobile이지만 뺵업 느낌으로 놔둠
    path('signup', mobileViews.signup, name='signup'),
    path('login', mobileViews.login, name='login'),
    path('updateUserinfo', mobileViews.updateUserinfo, name='updateUserinfo'),
    path('checkUser', mobileViews.checkUser, name='checkUser'),
    path('checkEmail', mobileViews.checkEmail, name='checkEmail'),
    path('walletAddrAdd', mobileViews.walletAddrAdd, name='walletAddrAdd'),
    path('userLoginDateUp', mobileViews.userLoginDateUp, name='userLoginDateUp'),
	path('checkOTPCode', mobileViews.checkOTPCode, name='checkOTPCode'),
	path('otpCodeSave', mobileViews.otpCodeSave, name='otpCodeSave'),
    # -------------------------------------------------------------------------------


    # -------------------------------------------------------------------------------
    # admin
    path('userManageHtml', views.userManageHtml, name='userManageHtml'),
    path('userDetailHtml', views.userDetailHtml, name='userDetailHtml'),

    # 2021.12.28 HSW 작성 - Admin -> 멤버관리 -> 작가관리 -----
    path('authorManageHtml', views.authorManageHtml, name='authorManageHtml'),
    path('authorDetailHtml', views.authorDetailHtml, name='authorDetailHtml'),

    # HSW 작성 끝 --------------------------------------------




    # -------------------------------------------------------------------------------
]
