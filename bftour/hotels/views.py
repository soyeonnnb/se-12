from django.shortcuts import render, redirect
from .models import Post, Hotel, RoomType
from .forms import MakeHotel
from rooms.models import Room
from django.utils import timezone

# Create your views here.
def index(request):
    hotels = Hotel.objects.all()
    context = {'hotels': hotels}
    return render(request, 'hotels/index.html',context)

def blog(request):
    #모든 Post를 가져와 list에 저장하고 페이지를 열때 list로 가져오게 함
    if request.method == 'POST':
        form = MakeHotel(request.POST, request.FILES)
        
        if form.is_valid():
            forms = form.save(commit=False)
            forms.save()
            return redirect("/index")  
    else:
        form = MakeHotel()      
    
    return render(request, 'hotels/blog.html', {'form':form})
 
#게시글(posting)을 부르는 posting 함수
def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    hotels = Hotel.objects.get(pk=pk)
    rooms= Room.objects.filter(hotel=pk)
    types=hotels.type.all()
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'hotels/posting.html', {'hotels':hotels, 'rooms':rooms,'types':types})

