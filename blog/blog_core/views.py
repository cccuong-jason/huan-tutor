import json
import io

from django.views import generic
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.models import User
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

# so sanh 2 san pham
# goi toi machine learning model
# nhan dang do noi that

#WHERE Status = "1"

def get_product(request):
	'''
	Lấy được tất cả bài viết
	'''
	if request.method == 'GET':

		data = list(Post.objects.filter(status=1).filter(is_deleted=False).values())

	return JsonResponse(data, safe=False)
		
		

@csrf_exempt
def create(request):

	if request.method == 'POST':

		data = request.body
		#byte
		fix_bytes_value = data.decode('utf8').replace("'", '"')
		data = json.loads(fix_bytes_value)
		result = json.dumps(data, indent=4, sort_keys=True)
		# result(string)
		result = json.loads(result)
		# convert string -> json

		post = Post.objects.filter(title=result["title"]).first()

		if post:

			response = {"data": "Post đã tồn tại", "message": "Thất bại"}

		else:

			user = User.objects.filter(id=result["author"]).first()

			if user:

				result["author"] = user
				post = Post.objects.create(**result)
				post.save()
				response = {
					"data": post.title,
					"message": "Tạo post mới thành công"
				}

			else:

				response = {
					"message": "Thất bại",
					"data": "Người viết không tồn tại dữ liệu"
				}

	return JsonResponse(response, safe=False)

@csrf_exempt
def update(request, slug):

	if request.method == "PUT":

		data = request.body

		fix_bytes_value = data.decode('utf8').replace("'", '"')
		data = json.loads(fix_bytes_value)
		result = json.dumps(data, indent=4, sort_keys=True)
		result = json.loads(result)

		post = Post.objects.filter(slug=slug).first()

		if not post:

			response = {"data": "Post bạn muốn update không tồn tại", "message": "Thất bại"}

		else:

			#static
			# keys = ["title", "slug", "author", "content", "status"]
			# for key in result:
			# 	if key in keys:
			# 		print("Key: ", key)
			# 		print(result[key])
			# 		post.key = result[key]
			# 		post.save()
			# 		print(post.key)
			
			# print(post.title)
				
			#dynamic
			post = Post.objects.filter(slug=slug).update(**result)
			print(post)
			# post.title = result['title']
			response = {
				# "data": post.title,
				"message": "Update post thành công"
			}

	return JsonResponse(response, safe=False)

@csrf_exempt
def delete(request, slug):

	if request.method == "DELETE":

		post = Post.objects.filter(slug=slug).first()

		if not post:

			response = {"data": "Post bạn muốn xóa không tồn tại", "message": "Thất bại"}

		else: 

			post.is_deleted = True
			post.save()
			response = {"data": "Post đã được xóa thành công", "message": "Thành công"}

	return JsonResponse(response, safe=False)



