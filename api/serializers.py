from rest_framework import serializers
from .models import Article,Commenting
from django.contrib.auth.models import  User
from rest_framework.authtoken.views import Token

class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ['id', 'title', 'description', 'likes','userid', 'date']
        

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Commenting
        fields = ['id', 'article_id', 'userid', 'comments', 'date']
        
    
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        
        extra_kwargs = {
            'password':{
                'write_only': True, 
                'required' : True
            }
        }

    #overriding the user model      
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user