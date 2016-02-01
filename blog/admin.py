from django.contrib import admin
from blog.models import Post, Comment, Tag, Category, Guest_book
#from blog.models import Guest_book

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'get_title_length']
    #이걸 쓰니까 포스트 위에 아이디라고 뜬다...근데 이게 무슨 얘기?
    list_display_links = ['title']
    #link to title!!

    def get_title_length(self, post):
        return len(post.title)

class Guest_bookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']





admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Guest_book, Guest_bookAdmin)

