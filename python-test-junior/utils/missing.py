import json

def find_missing(delivery_list, bag):
  s=[]
  f = open('data/items.json','r')
  data=f.read()
  obj=json.loads(data)
  for j in delivery_list:
     if j not in bag:
      for i in obj:
        if i['id']==j:
          s.append(i)
  return s