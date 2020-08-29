from django import template

register = template.Library()

from ..models import Post
@register.simple_tag
def total_posts():
    return Post.objects.all().filter(status="published").count()

@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.objects.all().filter(status="published").order_by('-publish')[:count]
    return {'latest_posts': latest_posts}
