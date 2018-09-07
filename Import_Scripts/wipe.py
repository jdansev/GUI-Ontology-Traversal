from GUI.models import Attack_Node, Defense_Node, Comment
Attack_Node.objects.all().delete()
Defense_Node.objects.all().delete()
Comment.objects.all().delete()
print("Done.")
