from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404  
from django.urls import reverse
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.urls.base import reverse_lazy
from django.views.generic import View, FormView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

from . import forms 
from . import models
from . import mixins

from django.http import HttpResponse

# # 예약자 정보
# @login_required
# def booker_info_view(request):
#     booker = request.user
#     booker_info = User.objects.get(pk=booker.pk)
#     return render(request, "payments/paymentdetail.html", {"booker_info":booker_info})




# def payment_detail_view(request):
#    form = PaymentForm()
#    if request.method == "POST":
#       form = PaymentForm(request.POST)
#       if form.is_valid:
#          return HttpResponseRedirect(reverse('payments.html')) 
#    errors = form.errors or None 
#    return render(request, 'payments.html',{
#           'form': form,
#           'errors': errors,
#    }) #     return render(request, "payments/paymentdetail.html", {"payment":payments_type})
#         # else : 
#         #      return render(request, "payments/paymentdetail.html", {"payment":payments_type})
            
        
#         # if PaymentForm.is_valid():
#         #     messages.success(request, '결제가 완료되었습니다.')
#         #     return render(request, "payments.html", {"payment":payments_type})
#         # else : 
#         #     messages.error(request, '결제가 취소되었습니다.')
#         #     return redirect(reverse("payments.html"))
    
        
# def load_payments(request): 
#     payments = Payment.objects.all() 
#     content = {'payments':payments}
#     return render(request, "payments.html", content) 
