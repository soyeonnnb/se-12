from django.shortcuts import render

from .models import Post, tb_product

# Create your views here.
def index(request):
    hotels = tb_product.objects.all()
    context = {'hotels': hotels}
    return render(request, 'hotels/index.html',context)

def blog(request):
    postlist = Post.objects.all()
    #모든 Post를 가져와 list에 저장하고 페이지를 열때 list로 가져오게 함
    return render(request, 'hotels/blog.html', {'postlist':postlist})

#게시글(posting)을 부르는 posting 함수
def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    hotels = tb_product.objects.get(pk=pk)
     # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'hotels/posting.html', {'hotels':hotels})

