from django.urls import path
from . import views

urlpatterns=[
    path('api/users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/users/profile/',views.getUserProfile,name="user-profile"),
    path('api/users/',views.getUsers,name="users"),
    path('api/users/score/',views.addScore,name="addscore"),
    path('api/users/getallscore/',views.getAllScore,name="getAllScore"),
    path('api/users/register/',views.registerUser,name="register"),

    path('api/admin/setAverageValue/<str:value>',views.setAverageValue,name="setAverageValue"),
    path('api/admin/getAverageValue/<str:pk>',views.getAverageValue,name="setAverageValue"),
    path('api/admin/winningValue/',views.getWinningValue,name="getWinningValue"),
]