from django.shortcuts import render
from django.http import JsonResponse
from .models import Article


def article_list_html(request):
  articles = Article.objects.all()
  context = {"articles": articles}
  return render(request, "articles/article_list.html", context)

def json_01(request):
  articles = Article.objects.all()
  json_res = []

for article in articles:
  json_res.append(
    {
      "title": article.title,
      "content": article.content,
      "created_at": article.created_at,
      "updated_at": article.updated_at,
    }
  )

  return JsonResponse(json_res, safe=False)