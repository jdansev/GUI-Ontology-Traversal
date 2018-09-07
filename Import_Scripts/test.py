from GUI.models import Attack_Node, Defense_Node
import glob


print("Test #1: check attack nodes for discrepancies between number of raw files and django imported data.")
print("Note: if there are files that are duplicates and should not be displayed in the ontology, this will be the count offset of the results")

raw_files=len(glob.glob("Import_Scripts/Data_MainNodes/*.txt"))
print("Number of raw text files: ", raw_files)
db_files=Attack_Node.objects.count()
print("Number of django imported data: ", db_files)
if raw_files == db_files:
    print("\nTEST PASSED")
else:
    print("\nTEST FAILED")

print("\n")

print("Test #2: Check defense nodes for discrepancies between number of raw files and django imported data.")
raw_files=len(glob.glob("Import_Scripts/Data/*.txt"))
print("Number of raw text files: ", raw_files)
db_files=Defense_Node.objects.count()
print("Number of django imported data: ", db_files)

if raw_files == db_files:
    print("\nTEST PASSED")
else:
    print("\nTEST FAILED")

print("\nTesting done.")

