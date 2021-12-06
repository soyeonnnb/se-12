from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404  
from django.urls import reverse
from django.contrib import messages

from .forms import PaymentForm 
from .models import Payment

from django.http import HttpResponse

def payment_detail_view(request):
   form = PaymentForm()
   if request.method == "POST":
      form = PaymentForm(request.POST)
      if form.is_valid:
         #redirect to the url where you'll process the input
         return HttpResponseRedirect('payments.html') # insert reverse or url
   errors = form.errors or None # form not submitted or it has errors
   return render(request, 'payments.html',{
          'form': form,
          'errors': errors,
   })



        # if form.is_valid():
        #     payments_type = request.POST["payment"]
        #     payments_type = Payment.objects.all
        #     return render(request, "payments/paymentdetail.html", {"payment":payments_type})
        # else : 
        #      return render(request, "payments/paymentdetail.html", {"payment":payments_type})
            
        
        # if PaymentForm.is_valid():
        #     messages.success(request, '결제가 완료되었습니다.')
        #     return render(request, "payments.html", {"payment":payments_type})
        # else : 
        #     messages.error(request, '결제가 취소되었습니다.')
        #     return redirect(reverse("payments.html"))
    
        
def load_payments(request): 
    payments = Payment.objects.all() 
    content = {'payments':payments}
    return render(request, "payments.html", content) 
