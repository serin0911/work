from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    # views.post_list 함수는 등록된 포스트를 보는 함수로 DB에서 필요한 데이터를 가져와서, post_list.html에게 데이터를 넘겨주어야함
    # 게시글이 등록된 날짜가 현재 날짜보다 이전으로 들어있는 행만 검색
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    # render()를 호출하여 화면을 출력(화면을 그리는 일을 한다)
    # render()에게 사용자가 요청한 정보를 전달한다(해당 매개변수가 request이며, post_list가 전달 받은 것을 화면 그릴 때, 필요할 수 있으니 전달하는 것이다.)
    # 'blog/post_list.html'이 화면을 그리도록 지정한다.(화면 출력 주체 지정)
    # {'posts': posts}를 통해 화면 출력에 사용할 데이터(posts)를 전달