from rest_framework import serializers
from apps.news.models import News,Feedback


class NewsSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        context = kwargs.get('context')
        if context:
            self.request = context.get('request')

    class Meta:
        model =News
        fields =('pk','title','article','category')


    def create(self, validate_data):
        news =News(**validate_data)
        news.author=self.request.user
        news.save()
        return news

class CommentSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        context = kwargs.get('context')
        if context:
            self.request = context.get('request')
    class Meta:
        model=Feedback
        fields =('pk','comment')

    def create(self, validated_data):
        comment=Feedback(**validated_data)
        comment.commentator= self.request.user
        comment.news=self.request.news
        comment.save()
        return comment