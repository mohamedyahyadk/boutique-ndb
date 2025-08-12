
from django.urls import path
from ndb_app.views import index ,product_details ,generate_qr, qr_page

urlpatterns=[
    # path('',home,name='ndb_app'),
    path('',index,name='index'),
    path('qr/', qr_page, name='qr_page'),
    path('<pk>/',product_details ,name='product_details'),
    path('generate_qr/<path:url_path>/', generate_qr, name='generate_qr'),
]
