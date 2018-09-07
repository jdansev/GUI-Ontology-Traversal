import json
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Attack_Node, Defense_Node, Comment
from datetime import datetime

# My views

def index(request):
	d_nodes = Defense_Node.objects.all()
	a_nodes = Attack_Node.objects.all()
	comments = Comment.objects.all()
	return render(request, "GUI/index.html", {"d_nodes" : d_nodes, "a_nodes" : a_nodes, "comments" : comments })

def add_node(request):
	if request.method == 'POST':
		defense = request.POST['name']
		attack = request.POST['link']
		desc = request.POST['desc']
		print("Added a new node.")
		Attack_Node.objects.get_or_create(name=attack)
		n = Defense_Node(name=defense, desc=desc, parent=Attack_Node.objects.get(name=attack))
		n.save()
		return HttpResponseRedirect('/')
	d_nodes = Defense_Node.objects.all()
	a_nodes = Attack_Node.objects.all()
	return render(request, "GUI/index.html", {"d_nodes" : d_nodes, "a_nodes" : a_nodes})


def add_comment(request, id):
	if request.method == 'POST':
		text = request.POST.get('comment_text')
		c = Comment(text=text, parent=Defense_Node.objects.get(id=id))
		c.save()
	return HttpResponse(json.dumps({}), content_type="application/json")

def download_comments(request):
	comment_list = Comment.objects.all()
	attack_list = {}
	for comment in comment_list:
		if comment.parent not in attack_list:
			attack_list[comment.parent] = [[comment.pub_date, comment.text]]
		else:
			attack_list[comment.parent].append([comment.pub_date, comment.text])
	respone_text = "Comment log downloaded at " + datetime.now().strftime('%d-%m-%y %H:%M') + "\nTotal: " + str(len(comment_list)) + "\n\n"
	for a in attack_list:
		respone_text += str(a) + ":\n"
		for c in attack_list[a]:
			respone_text += "\t[" + c[0].strftime('%d-%m-%y %H:%M') + "] " + c[1] + "\n"
	response = HttpResponse(respone_text, content_type='text/plain')
	response['Content-Disposition'] = 'attachment; filename=Comments_List.txt'
	return response
