from books.models import Book as BookModel
from spyne.util.django import DjangoComplexModel


class Book(DjangoComplexModel):
    class Attributes(DjangoComplexModel.Attributes):
        django_model = BookModel