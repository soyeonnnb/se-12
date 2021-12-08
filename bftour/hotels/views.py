from django.shortcuts import render, redirect
from .models import Hotel
from .forms import MakeHotel, MakeRoom
from rooms.models import Room


# Create your views here.
def index(request):
    hotels = Hotel.objects.all()
    context = {'hotels': hotels}
    return render(request, 'hotels/index.html',context)

def makehotels(request):
    if request.method == 'POST':
        form = MakeHotel(request.POST, request.FILES)
        form2 = MakeRoom(request.POST)
        
        if form.is_valid():
            forms = form.save(commit=False)
            forms.facility = request.POST.getlist('types[]')
            forms.reg_id = request.user.id
            forms.save()
              
        if form2.is_valid():
            forms2 = form2.save(commit=False)
            forms2.room_name = request.POST.getlist('roomNm');
            forms2.price = request.POST.getlist('room_price');
            forms2.hotel_id = forms.id
            forms2.user_id = request.user.id
            forms2.save()
            
        return redirect("/index") 
    else:
        form = MakeHotel()    
        form2 = MakeRoom()
    
    return render(request, 'hotels/makehotel.html', {'form':form, 'form2':form2})
 
def viewhotel(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    hotels = Hotel.objects.get(pk=pk)
    rooms= Room.objects.filter(hotel=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'hotels/viewhotel.html', {'hotels':hotels, 'rooms':rooms})

