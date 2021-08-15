import json
 
f= open('json/Universidad de Antioquia_7.json',)
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
fout=open("csv/prod/Universidad de Antioquia.csv","a",encoding="utf-8")

for element in data['content']:
    new_line = element['name']+',,'+str(element['durationHours'])+',\n'
    fout.write(new_line)
