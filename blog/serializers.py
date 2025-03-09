from rest_framework import serializers
from .models import Post, Category, Tag

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'content', 'author', 'category', 'tags', 'status', 'thumbnail', 'created_at', 'updated_at']

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        tags_data = validated_data.pop('tags')
        
        category, created = Category.objects.get_or_create(**category_data)
        post = Post.objects.create(category=category, **validated_data)
        
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(**tag_data)
            post.tags.add(tag)
        
        return post

    def update(self, instance, validated_data):
        category_data = validated_data.pop('category')
        tags_data = validated_data.pop('tags')

        # Update category
        category, created = Category.objects.get_or_create(**category_data)
        instance.category = category

        # Update tags
        instance.tags.clear()
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(**tag_data)
            instance.tags.add(tag)

        # Update other fields
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.status = validated_data.get('status', instance.status)
        instance.thumbnail = validated_data.get('thumbnail', instance.thumbnail)
        instance.save()

        return instance