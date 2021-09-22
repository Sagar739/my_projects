from django.urls import path, include
from demo import views

app_name='demo'

urlpatterns = [
    # path('index/',views.displayData,name="displayData"),
    path('personregister/',views.register_person,name='register_person'),
    path('register/', views.postParticipant, name = "postParticipant"),
    path('student/',views.student_data,name="student_data"),
]