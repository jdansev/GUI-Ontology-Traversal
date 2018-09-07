import glob
import json
import codecs

# import django model
from GUI.models import Attack_Node, Defense_Node

def remove_duplucates(name):
    # remove byte order mark character
    name = name.replace(u'\ufeff', '')
    if name == "denial-of-service" or name == "dos/ddos" or name == "denial of service":
        name = "dos"
    elif name == "ddos" or name == "distributed denial of service":
        name = "DDos"
    name = name.capitalize()
    return name

def remove_encoding(text):
    text = text.replace('\r','')
    text = text.replace('\n','')
    text = text.replace('\ufeff','')
    text = text.replace('\u00a9','')
    return text

def parse_line(line):
    import re
    # get first line of string
    first_line = line.partition("\n")[0]
    # find the index of first digit occurence
    m = re.search("\d", first_line)
    # get substring, trim whitespace, and convert to lowercase
    attack_name = first_line[0:m.start()].strip().lower()
    # removing known duplicates
    attack_name = remove_duplucates(attack_name)
    attack_name = attack_name.title()
    return attack_name

def fix_punctuation(text):
    import re
    brackets = re.findall(r"\((.*?)\)", text)
    trim_brackets = [string.strip() for string in brackets]
    for a, b in zip(brackets, trim_brackets):
        text = text.replace(a, b, 1)
    periods = re.findall(r" *\. *", text)
    for p in periods:
        text = text.replace(p, ". ", 1)
    commas = re.findall(r" *, *", text)
    for c in commas:
        text = text.replace(c, ", ", 1)
    text = remove_encoding(text)
    return text


files=glob.glob("./Data/*.txt") # text files are stored here
files_desc=glob.glob("./Data_MainNodes/*.txt") # text files of main nodes with descriptions of attacks
j_path='data.json'
hm={} # hm<(string) name, [(string) main node description, ((string)link, (string[])link description)]

# read in from desc files (main nodes)
# for df in files_desc:
#     f_in=codecs.open(df,encoding="utf-8",mode='r')

#     name=parse_line(f_in.readLine()) # first line node name
#     f_in.readLine()
#     desc=fix_punctuation(f_in.read()) # rest of file

#     print("---",desc,"---")

#     if hm.get(name) is None: # new entry
#         hm[name]=[desc,[]]
#     else:
#         temp=hm.get(name)
#         empty=[]
#         temp[0]=desc
#         temp[1]=empty

attack_list = {}

print(files_desc)

for file in files_desc:
     with codecs.open(file, "r",encoding='utf-8', errors='ignore') as f:
        data=[""]*2
        c=0
        for line in f:
            if line!="\r\n":
                data[c]=data[c]+line
            else:
                c+=1
        name=data[0].strip().lower().title()
        name=remove_encoding(name)
        desc=fix_punctuation(data[1])
        attack_list[name] = desc



# read in from all files
for file in files:
        data=[""]*3
        f_in=codecs.open(file,encoding="utf-8",mode='r')
        c=0
        for line in f_in:
            if line!="\r\n":
                data[c]=data[c]+line
            else:
                c+=1
        name=parse_line(data[0])
        link=data[1].strip().capitalize()
        link = fix_punctuation(link)
        desc=data[2:]
        cat_desc=""
        for i in desc:
            cat_desc+=i
        cat_desc = fix_punctuation(cat_desc)
        if hm.get(name) is None: # new entry
            if name in attack_list:
                attack_desc = attack_list[name]
            else:
                print("ATTACK NOT FOUND:",name)
                attack_desc = "No description available."
            hm[name]=[attack_desc,[(link,cat_desc)]]
        else:
            temp=hm.get(name)
            (temp[1]).append([link,cat_desc])
        print(cat_desc)
        # save as a new entry in django model
        # Attack_Node.objects.get_or_create(name=name)
        # n = Defense_Node(name=link, desc=cat_desc, parent=Attack_Node.objects.get(name=name))
        # n.save()

# uncomment to put into JSON
# with open(j_path,'w') as f_out:
#     json.dump(hm,f_out)


