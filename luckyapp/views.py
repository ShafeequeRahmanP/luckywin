from django.shortcuts import render,HttpResponse
from .models import Lottey_Result_2PM,Lottey_Result_5PM,Stockist_Model
from django.views.generic import ListView,TemplateView,View
from datetime import date
from .forms import StockistForm
from django.shortcuts import redirect
from django.template.context_processors import csrf
# from django.template.loader import get_template
# from .utils import render_to_pdf 
import datetime









def index_view(request):
    return render(request,'index.html')


def todayresult_view(request):
    return render(request,'todayresults.html')

def oldresult_view(request):
    return render(request,'oldresult.html')

# def stockistship_view(request):
#     return render(request,'stockistship.html')

# def result_view(request):
#     return render(request,'result.html')



class ResultView2(ListView):
    template_name = "result2pm.html"

    def get_queryset(self):
        obj = Lottey_Result_2PM.objects.all()
        return Lottey_Result_2PM.objects.all()[obj.count()-1:obj.count()]
        # return Lottey_Result.objects.all()[:1]
        # obj= Lottey_Result.objects.filter(testfield=12).order_by('-id')[0]
        # return Lottey_Result.objects.latest("date")

class ResultView5(ListView):
    template_name = "result5pm.html"

    def get_queryset(self):
        obj = Lottey_Result_5PM.objects.all()
        return Lottey_Result_5PM.objects.all()[obj.count()-1:obj.count()]

        


    
    
# def oldd(request):
#     l2result = Lottey_Result_2PM.objects.all()
#     MyFilter = LotteryFilter(request.GET, queryset = l2result) 
#     l2result = MyFilter.qs
#     context = {'l2result':l2result, 'MyFilter':MyFilter}
#     return render (request, "result2_1pm.html", context)


class ResultView5_1(ListView):
    template_name = "result5_1pm.html"

    def get_queryset(self):
        obj = Lottey_Result_5PM.objects.all()
        if(obj.count()>9):
            return Lottey_Result_5PM.objects.all()[obj.count()-9:obj.count()]
        else:
            return Lottey_Result_5PM.objects.all()
        




class ResultView2_1(ListView):
    template_name = "result2_1pm.html"
    form = Lottey_Result_2PM()
    # yr = form.date.year
    # import pdb
    # pdb.set_trace()
    # def post(self,request):
    #     dat = request.POST.get('dat')
    def get_queryset(self):
        
        # return  Lottey_Result_2PM.objects.filter(date__year='2020', 
        #               date__month='09', date__day='10')
        obj = Lottey_Result_2PM.objects.all()
        if(obj.count()>10):
            return Lottey_Result_2PM.objects.all()[obj.count()-10:obj.count()]
        else:
            return Lottey_Result_2PM.objects.all()





def stockistship_view(request):
    if request.method == 'GET':
        form = StockistForm()
    else:
        form = StockistForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            agency_name = form.cleaned_data['agency_name']
            contact_number_1 = form.cleaned_data['contact_number_1']
            contact_number_2 = form.cleaned_data['contact_number_2']
            email = form.cleaned_data['email']
            street = form.cleaned_data['street']
            district = form.cleaned_data['district']
            state = form.cleaned_data['state']
            pincode = form.cleaned_data['pincode']
            existing_stocklist_status = form.cleaned_data['existing_stocklist_status']
            stockist_type = form.cleaned_data['stockist_type']

            p = Stockist_Model(name = name, agency_name = agency_name, contact_number_1 = contact_number_1, contact_number_2 = contact_number_2, email = email, street = street, district = district, state = state, pincode = pincode, existing_stocklist_status = existing_stocklist_status, stockist_type =stockist_type )
            p.save()
            return HttpResponse('success')
            # try:
            #     send_mail(subject, 'hi' + first_name, 'shafeequerahman782@gmail.com', [email])
            # except BadHeaderError:
            #     return HttpResponse('Invalid header found.')
            
            # return HttpResponse('success')
    return render(request, "stockistship.html", {'form': form})




class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        obj = Lottey_Result_2PM.objects.all()
        ob = Lottey_Result_2PM.objects.all()[obj.count()-1:obj.count()]
        data = {
             'today': datetime.date.today(), 
             'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        #getting the template
        pdf = render_to_pdf('pdf.html',data) 
        #rendering the template
        return HttpResponse(pdf, content_type='application/pdf')









































# def lottery(request):
#     obj = Lottey_Result.objects.get(id=1)
#     # context = {
#     #     'first': obj.first_price,
#     #     'second': obj.second_price
        
#     # }
#     context = {
#         'object':obj.get.all()
        
#     }
#     return render(request, "result.html", context)