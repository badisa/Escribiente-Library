from api.models import Book
from rest_framework import serializers


class BookSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=80)
    copies = serializers.IntegerField(required=False)
    checked_out = serializers.IntegerField(required=False)
    descript = serializers.CharField(required=False)
    published = serializers.CharField(max_length=30, required=False)
    cover = serializers.CharField(required=False)
    isbn_13 = serializers.CharField(max_length=13, required=False)
    isbn_10 = serializers.CharField(max_length=10, required=False)
    isbn = serializers.CharField(max_length=13, required=False)
    note = serializers.CharField(required=False)

    def create(self, validated_data):
        return Book.objects.new_book(
            validated_data.get('isbn'), note=validated_data.get('note', ''))

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.copies = validated_data.get('copies', instance.copies)
        instance.checked_out = validated_data.get('checked_out', instance.checked_out)
        instance.descript = validated_data.get('description', instance.descript)
        instance.cover = validated_data.get('cover', instance.cover)
        instance.note = validated_data.get('note', instance.note)
        instance.save()
        return instance
