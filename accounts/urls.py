from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_view
from rest_framework import routers


app_name = 'accounts'

urlpatterns = [
    path('get_token_auth/', auth_view.obtain_auth_token)
]

router = routers.SimpleRouter()
router.register('user',views.UserViewSet)

urlpatterns += router.urls
