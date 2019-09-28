import graphene
from schools.models import School
from graphene_django.types import DjangoObjectType
from django.db.models import Q

class SchoolNode(DjangoObjectType):
    class Meta:
        model = School


class Query(graphene.ObjectType):
    schools = graphene.List(
        SchoolNode,
        first=graphene.Int(),
        skip=graphene.Int(),
    )


    def resolve_schools(self, info, first=None, skip=None, **kwargs):
        schools = School.objects.all()

        if skip:
            schools = schools[skip:]
        if first:
            schools = schools[:first]

        return schools
