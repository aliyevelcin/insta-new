from django.urls import path
from core.views import MainView , ExploreView ,StoryView , PostView
 

app_name = 'core'


urlpatterns = [
    path('',MainView.as_view(),name ='main'),
    path('exp/',ExploreView.as_view() ,name ='explore'),
    path('story/',StoryView.as_view() ,name ='story'),
    path('post/',PostView.as_view() ,name ='post'),
     

]