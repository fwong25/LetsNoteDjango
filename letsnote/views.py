from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Note
from datetime import datetime

def list_note_items(request):
    note_list = Note.objects.all()
    context = {'note_list' : note_list[::-1]}
    return render(request, 'letsnote/note_list.html', context)

def insert_note_item(request:HttpRequest):
    today_date = datetime.today().strftime('%Y-%m-%d')
    note = Note(title = request.POST['title'], content = request.POST['content'], created_date = today_date, last_modified_date = today_date)
    note.save()
    return redirect('/letsnote/list/')

def modify_note_item(request:HttpRequest, note_id):
    note_list = Note.objects.all()
    context = {'note_list' : note_list[::-1], 'note_id' : note_id}
    return render(request, 'letsnote/note_modify.html', context)

def modify_note_item_action(request:HttpRequest, note_id):
    if request.POST['action'] == 'Cancel':
        return redirect('/letsnote/list/')
    
    today_date = datetime.today().strftime('%Y-%m-%d')
    note_to_modify = Note.objects.get(id=note_id)
    note_to_modify.title = request.POST['title']
    note_to_modify.content = request.POST['content']
    note_to_modify.last_modified_date = today_date
    note_to_modify.save()
    return redirect('/letsnote/list/')

def delete_note_item(request, note_id):
    note_to_delete = Note.objects.get(id=note_id)
    note_to_delete.delete()
    return redirect('/letsnote/list/')
