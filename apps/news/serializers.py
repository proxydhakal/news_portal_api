from rest_framework import serializers
from apps.news.models import News,Feedback,Favorite
from django.shortcuts import render,get_object_or_404
class CommentSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # print('kwargs',kwargs)
        self.kwargs=kwargs
        context = kwargs.get('context')
        # print('context',context)
    
        if context:
            # print(dir(context.get('view')))
            # print(context.get('view').kwargs)
            self.request = context.get('request')
            self.parms=context.get('view').kwargs
    class Meta:
        model=Feedback
        fields =('pk','comment',)

    def create(self, validated_data):
        comments=Feedback(**validated_data)
        comments.commentator= self.request.user
        comments.news = get_object_or_404(News,pk=self.parms.get('pk'))
        comments.save()
        return comments

class FavoriteSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.kwargs=kwargs
        context = kwargs.get('context')
    
        if context:
            self.request = context.get('request')
            self.parms=context.get('view').kwargs
    class Meta:
        model=Favorite
        fields =('pk','is_favorite',)

    def create(self, validated_data):
        favorites=Favorite(**validated_data)
        favorites.author= self.request.user
        favorites.news = get_object_or_404(News,pk=self.parms.get('pk'))
        favorites.save()
        return favorites

class NewsSerializer(serializers.ModelSerializer):
    comments= CommentSerializer(many=True)
    favourite_news=FavoriteSerializer()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        context = kwargs.get('context')
        if context:
            self.request = context.get('request')

    class Meta:
        model =News
        fields =('pk','title','article','category','comments','likes')


    def create(self, validate_data):
        news =News(**validate_data)
        news.author=self.request.user
        news.save()
        return news

