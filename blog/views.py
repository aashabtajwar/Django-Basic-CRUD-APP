from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from . models import Post

# django rest framework libraries
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PostSerializer

# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        "name": "Aashab",
        "roll" : "1831019",
        "department" : "MTE",
        "batch" : "2k18"
    }
    return Response(api_urls)


@api_view(['GET'])
def getPosts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True) # serializing many objects
    return Response(serializer.data)

@api_view(['GET'])
def getOnePost(request, pk):
    posts = Post.objects.get(id=pk)
    serializer = PostSerializer(posts, many=False) # serializing many objects
    return Response(serializer.data)


# post
@api_view(['POST'])
def writeBlogPost(request):
    serializer = PostSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# update

@api_view(['PUT'])
def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(instance=post, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# delete
@api_view(['DELETE'])
def deletePost(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return Response("Blog post deleted")


#def getPosts(request):
#    blog_posts = Post.objects.all()
#    return HttpResponse(blog_posts)

# defining home route
def home(request):
    return HttpResponse('Home')

# about route
def about(request):
    return JsonResponse({"information": "test"})

# writing a blog route
def writeBlog(request):
    
    #posts = Post.objects.filter(title="Blog title").first()
    #posts = get_object_or_404(Post, pk=1)
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

def writepost(request):
    if request.method == 'POST':
        q = Post(title = request.POST.get('title'), description = request.POST.get('description'), content = request.POST.get('content'), pub_date=timezone.now())
        q.save()
        return HttpResponse(q.content)
    else:
        return render(request, 'blog/file.html')

# route to display each blog
# editing a blog
# deleting blog