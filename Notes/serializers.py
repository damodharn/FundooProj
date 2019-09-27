from rest_framework import serializers
from rest_framework.response import Response
from .models import FundooNotes


class NoteSerializer(serializers.ModelSerializer):
    # serializer for serializing the data of the model

    class Meta:
        model = FundooNotes
        fields = ('id', 'title', 'note', 'reminder', 'collaborator', 'color', 'image')

    def create(self, data):
        print(type(data))
        print('Data', data)
        # method for the creation of the notes  with getting the particular user
        notes = FundooNotes(
            user=data['id'],
            title=data['title'],
            note=data['note'],
            reminder=data['reminder'],
            collaborator=data['collaborator'],
            color=data['color'],
            image=data['image'],
            archive=data['archive'],
        )
        notes.save()  # saving the note
        return True

    def delete(self, data=None, pk=None):
        if pk is None:
            title = data['title']
            try:
                id = FundooNotes.objects.get(title=title)
                id.delete()
            except TypeError:
                FundooNotes.objects.filter(pk).delete()

            except Exception as e:
                print(e)
                return Response({'message':'id not present'})
        else:
            try:
                id = FundooNotes.objects.get(id=pk)
                id.delete()
            except Exception as e:
                print(e)
                return e

    def get_id(self):
        return self.id
