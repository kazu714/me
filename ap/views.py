#<アプリ名>/views.py
# ListViewとDetailViewを取り込み
from django.views.generic import ListView, DetailView

# 自分で作ったPostモデルを取り込み
from .models import Post

# 一覧
class Index(ListView):
    # 一覧するモデルを指定 -> `object_list`で取得可能
    model = Post

# 個別
class Detail(DetailView):
    # 詳細表示するモデルを指定 -> `object`で取得可能
    model = Post
    

from django.views.generic.edit import CreateView, DeleteView

class Create(CreateView):
    model = Post
    
    # 編集対象にするフィールド
    fields = ["title", "body",  "tags"]
    

from django.views.generic.edit import UpdateView, DeleteView, UpdateView

class Update(UpdateView):
    model = Post
    fields = ["title", "body", "tags"]
    
class Delete(DeleteView):
    model = Post
    success_url = "/"

class Update(UpdateView):
    model = Post
    fields = ["title","body","tags"]