from rest_framework import serializers

from .models import Category, Genre, Title


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug',)
        lookup_field = 'slug'
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug',)
        lookup_field = 'slug'
        model = Genre


class CategoryField(serializers.SlugRelatedField):
    def to_representation(self, value):
        serializer = CategorySerializer(value)
        return serializer.data


class GenreField(serializers.SlugRelatedField):
    def to_representation(self, value):
        serializer = GenreSerializer(value)
        return serializer.data


class TitleSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=True, )
    category = CategorySerializer()
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        fields = ('id', 'name', 'year', 'rating', 'description',
                  'genre', 'category')
        model = Title


class TitlePostSerializer(serializers.ModelSerializer):
    category = CategoryField(
        slug_field='slug',
        queryset=Category.objects.all(),
        required=False)
    genre = GenreField(
        slug_field='slug',
        queryset=Genre.objects.all(),
        many=True)

    class Meta:
        model = Title
        fields = '__all__'
