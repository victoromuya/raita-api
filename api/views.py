from django.shortcuts import render
from .serializers import ArticleSerializer, UserSerializer, CommentSerializer
from .models import Article, Commenting
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from  rest_framework import status
from rest_framework import generics, mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated


class ArticleViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    
class CommentViewset(viewsets.ModelViewSet):
    queryset = Commenting.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    
class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

"""
class ArticleList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

class ArticleDetail(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin):
    
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    lookup_field = 'id'
    
    def get(self, request, id):
        return self.retrieve(request, id=id)
    
    def put(self, request, id):
        return self.update(request, id=id)
    
    def delete(self, request, id):
        return self.destroy(request, id=id)
    



class ArticleList(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ArticleDetail(APIView):
    def get_object(self, id):
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, id):
        articles = self.get_object(id)
        serializer = ArticleSerializer(articles)
        
        return Response(serializer.data)
    
    def put(self, request, id):
        article = self.get_object(id)

        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self, request, id) :
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        
        return Response(serializer.data)
    
    elif request.method == 'POST':
        
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def article_details(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
       
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            
"""