from django.contrib import admin

from .models import Post, Test

# Register your models here.
class PostAdmin(admin.ModelAdmin):

	list_display = ('title', 'slug', 'status', 'created_at')
	list_filter = ("status",)
	search_fields = ['title', 'content']
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)

class TestAdmin(admin.ModelAdmin):

	readonly_fields = ('id',)
	
	class Meta:
		model = Test

admin.site.register(Test, TestAdmin)

