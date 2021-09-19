from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from apps.question.models import Question

class QuestionSerializer(serializers.ModelSerializer):
    text = serializers.CharField(required=True)
    
    class Meta:
        model = Question
        fields = ('text',)

    def create(self, validated_data):
        text = validated_data['text']

        try:
            text = Question.objects.get(text=text)
            
            return text
        except:
            raise serializers.ValidationError({"msg": "I'm sorry. I can't find your question."})
