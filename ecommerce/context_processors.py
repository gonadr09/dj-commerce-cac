from .models import Category, Tag
from datetime import datetime, timedelta


def categories_root(request):
    categories_root = Category.objects.filter(parent=None)
    return {'categories_root': categories_root}


def tags(request):
    tags = Tag.objects.filter()
    return {'tags': tags}
    

def a_week_ago(request):
    today = datetime.now()
    a_week_ago = today - timedelta(days=7)
    return {'a_week_ago': a_week_ago}