from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer
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


def json_02(request):
    articles = Article.objects.all()
    res_data = serializers.serialize("json", articles)
    return HttpResponse(res_data, content_type="application/json")


@api_view(["GET"])
def json_drf(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    # many=True 는 단일 객체가 아니라서 넣어준다. 단일객체면 지워주워도 된다.
    return Response(serializer.data)