from django.urls import path
from booking_app import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('rooms/', views.RoomList.as_view()),
    path('rooms/<int:pk>', views.RoomDetail.as_view()),
    path('facility/', views.FacilityList.as_view()),
    path('facility/<int:pk>', views.FacilityDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)