from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from notes.forms import NoteForm
from .models import Note

# Create your views here.
def home(request):
    form = NoteForm() #created an instance of the NoteForm to be used in the template for adding new notes
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = NoteForm()
    notes = Note.objects.all() #retrieved all the notes from the database using the Note model
    return render(request, 'home.html', {'notes': notes, 'form': form}) #rendered the home.html template and passed the notes and form to the template context

def delete_note(request,note_id):
    note = get_object_or_404(Note, id = note_id) #retrieved the note to be deleted using the get_object_or_404 shortcut function
    note.delete() #deleted the note from the database
    return redirect('home') #redirected the user back to the homepage after deleting the note

def update_note(request, note_id):
    note = get_object_or_404(Note, id = note_id) #retrieved the note to be updated using the get_object_or_404 shortcut function
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note) #created an instance of the NoteForm with the existing note data to be updated
        if form.is_valid():
            form.save( ) #saved the updated note to the database
            return redirect('home') #redirected the user back to the homepage after updating the note   