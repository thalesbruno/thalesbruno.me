from django.shortcuts import render
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from .models import Post
from home.models import Tag


def blog_home(request):
    tags = Tag.objects.all()

    post_list = Post.objects.order_by('-timestamp')
    paginator = Paginator(post_list, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'tags': tags,
    }
    return render(request, 'blog.html', context)