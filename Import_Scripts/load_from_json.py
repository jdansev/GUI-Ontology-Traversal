import json

# Import django model
from GUI.models import Attack_Node, Defense_Node

with open('data.json') as data_file:
	data = json.load(data_file)

for attack in data:
	print("-----",attack,"-----")
	attack_desc = data[attack][0]
	print(attack_desc)
	for defense in data[attack][1]:
		print("#####")
		link=defense[0]
		print("link:",link)
		defense_desc=defense[1]
		print("desc:",defense_desc)
		print("#####")
		
		# save as a new entry in django model
		Attack_Node.objects.get_or_create(name=attack, desc=attack_desc)
		n = Defense_Node(name=link, desc=defense_desc, parent=Attack_Node.objects.get(name=attack))
		n.save()

