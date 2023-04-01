from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_view
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = 'accounts'

urlpatterns = [
    path('get_token_auth/', auth_view.obtain_auth_token),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

router = routers.SimpleRouter()
router.register('user',views.UserViewSet)

urlpatterns += router.urls

# "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MDQxNTE5MiwiaWF0IjoxNjgwMzI4NzkyLCJqdGkiOiI0MWUyODAyNGMwODg0NWJlOWM4Y2ZhN2Q3NWY2NWM5NiIsInVzZXJfaWQiOjF9.WNhcSD6C8W25kV62RxmOYu97eR6NH-5kWhaVXeLSfMI",
# "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgwMzI5MDkyLCJpYXQiOjE2ODAzMjg3OTIsImp0aSI6IjY1YzZiOGYwY2M4ZDQwY2I5MTViMjZmYzdiODFiODNkIiwidXNlcl9pZCI6MX0.1zZBEZM1Yxkdox9OhbfQuyhsWO-B3bD70-W-hGRTrCA"