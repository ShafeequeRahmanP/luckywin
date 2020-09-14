from django.urls import path
from .views import index_view,stockistship_view,todayresult_view,oldresult_view,ResultView2,ResultView5,ResultView5_1,ResultView2_1
# from .views import GeneratePdf

urlpatterns = [
    path('',index_view, name='index'),
    path('today_result/',todayresult_view, name='today'),
    path('old_results/',oldresult_view, name='old'),
    path('stockistship/',stockistship_view, name='stockist'),
    path('result-2pm/',ResultView2.as_view(), name='result2'),
    path('result-5pm/',ResultView5.as_view(), name='result5'),
    path('result-5-1pm/',ResultView5_1.as_view(), name='result5-1'),
    path('result-2-1pm/',ResultView2_1.as_view(), name='result2-1'),
    # path('pdf/', GeneratePdf.as_view()),
    
    
    
]



app_name='luckyapp'