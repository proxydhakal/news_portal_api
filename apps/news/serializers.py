from rest_framework import serializers
from apps.news.models import News,Feedback
from django.shortcuts import render,get_object_or_404
class CommentSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('kwargs',kwargs)
        self.kwargs=kwargs
        context = kwargs.get('context')
        print('context',context)
        print(context['view'])
        if context:
            self.request = context.get('request')
    class Meta:
        model=Feedback
        fields =('pk','comment',)

    def create(self, validated_data):
        comments=Feedback(**validated_data)
        comments.commentator= self.request.user
        print('request',self.request.query_params)
        comments.news = get_object_or_404(News,pk=self.kwargs.get('pk'))
        print('news',comments.news)
        comments.save()
        return comments
class NewsSerializer(serializers.ModelSerializer):
    comments= CommentSerializer(many=True)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        context = kwargs.get('context')
        if context:
            self.request = context.get('request')

    class Meta:
        model =News
        fields =('pk','title','article','category','comments')


    def create(self, validate_data):
        news =News(**validate_data)
        news.author=self.request.user
        news.save()
        return news

