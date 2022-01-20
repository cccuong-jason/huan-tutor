import json
import io

from django.views import generic
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .models import Post, Test

# Create your views here.
# class PostList(generic.ListView):

# 	queryset = Post.objects.filter(status=1).order_by('created_at')
# 	template_name = 'index.html'

# class PostDetail(generic.DetailView):

# 	model = Post
# 	template_name = 'post_detail.html'

# class TestCreate(generic.CreateView):

# 	model = Test
# 	fields = ['title']

# 	def post(self, request, *args, **kwargs):
#         form = BookCreateForm(request.POST)
#         if form.is_valid():
#             book = form.save()
#             book.save()
#             return HttpResponseRedirect(reverse_lazy('books:detail', args=[book.id]))
#         return render(request, 'books/book-create.html', {'form': form})

def get_product(request):
	if request.method == 'GET':

		data = list(Post.objects.filter(status=1).order_by('created_at').values())
		print(data)

	return JsonResponse(data, safe=False)
		
		

@csrf_exempt
def create(request):
	if request.method == 'POST':

		data = request.body

		fix_bytes_value = data.decode('utf8').replace("'", '"')
		data = json.loads(fix_bytes_value)
		result = json.dumps(data, indent=4, sort_keys=True)
		# result(string)
		result = json.loads(result)
		# convert string -> json

		post = Test.objects.filter(title=result["title"]).first()

		if post:

			response = {"data": "Post đã tồn tại", "message": "Thất bại"}

		else:

			post = Test.objects.create(title=result["title"])
			post.save()
			response = {
				"data": post.title,
				"message": "Tạo post mới thành công"
			}

	return JsonResponse(response, safe=False)

@csrf_exempt
def update(request, id):

	if request.method == "PUT":

		data = request.body

		fix_bytes_value = data.decode('utf8').replace("'", '"')
		data = json.loads(fix_bytes_value)
		result = json.dumps(data, indent=4, sort_keys=True)
		# result(string)
		result = json.loads(result)
		# convert string -> json

		post = Test.objects.filter(id=id).first()

		if not post:

			response = {"data": "Post bạn muốn update không tồn tại", "message": "Thất bại"}

		else:

			post.title = result["title"]
			post.save()
			response = {
				"data": post.title,
				"message": "Update post thành công"
			}

	return JsonResponse(response, safe=False)

@csrf_exempt
def delete(request, id):

	if request.method == "DELETE":

		post = Test.objects.filter(id=id).first()

		if not post:

			response = {"data": "Post bạn muốn xóa không tồn tại", "message": "Thất bại"}

		else: 

			post.delete()
			response = {"data": "Post đã được xóa thành công", "message": "Thành công"}

	return JsonResponse(response, safe=False)



