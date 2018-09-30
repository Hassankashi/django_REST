from api.models import Note
note = Note(name="Mahsa", family ="Hassankashi")
note.save() 
Note.objects.all()
