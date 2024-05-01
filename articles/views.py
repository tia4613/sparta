from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer
from rest_framework import status
from rest_framework.views import APIView
from .models import Article




class ArticleListAPIView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "PUT", "DELETE"])
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
          serializer.save()
          return Response(serializer.data)

    elif request.method == "DELETE":
        article.delete()
        data = {"delete": f"Article({pk}) is deleted."}
        return Response(data, status=status.HTTP_200_OK)