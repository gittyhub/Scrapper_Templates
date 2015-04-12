import urllib
import re
from urllib.request import urlopen
from sys import argv

#--------gets the page-------
def get_page(url):
  try:
    return str(urlopen(url).read())
  except:
    return ""
  return index_site


#--------------gets all links for appartment----return list only 
def get_All_AppLinks(x):
  index_site = [] #<< creates an empty list
  Find_All_App_Listing = re.findall('[a-z]*/[a-z]*/[0-9]*.html', x) #<< x is the var where the main page of app is, not the webite 
  for a in Find_All_App_Listing:
    #job =  'http://sfbay.craigslist.com'+Find_All_App_Listing.group() #attachs the http start to the link completing the hyperlink 
    job =  'http://sfbay.craigslist.com'+'/'+a #attachs the http start to the link completing the hyperlink 
    if job in index_site:
      continue;
    else:
      index_site.append(job)
  return index_site

#--------------find CA from appartment link
def find_CA():
  q = open('FileOfAppendedList','r')
  g = open('Zipper','r')
  c = open('CA_Status','w')
  q1 = g.readlines()
  empty_list_for_CA = []
  for x in q1:
    try: 
    #c1 = re.search('CA ',x) or re.search('California',x)
    #print(str(c1.group()))
    #print(str(re.search('CA ',x).span())+'\n') 
      if 'CA' in x:
        c.write(str(re.search('CA ',x).span())+'\n')
      elif 'California' in x:
        c.write(str(re.search('California ',x).span())+'\n')
    except:
      #continue 
      c.write(x[:25]) 
      #print(x)
    #c.write(str(re.search('CA ',x))+'\n') 
    #c1 = re.search('CA ',x) 
  #find_CA = [x for x in q1[x] if 'CA' in q1[x]]
  '''for x in q1:
    if 'CA' in x:
      #empty_list_for_CA.append(x)
      c.write(x+'\n') 
    else:
      continue 
  for e in q1:
    if 'CA' not in x:
      #empty_list_for_CA.append(x)
      c1.write(e+'\n') 
    else:
      continue''' 
  #print(find_CA)
  '''i = get_page(x[0])
  p = 'CA' in i
  print(p)  
  print(x[0]) '''


#--------------Writes list to a file
def write_list_to_file(x):
  f = open('List2File', 'w')
  for i in x:
    f.write(i+'\n')
  f.close() 

#--------------Write entire posting to a file
def write_from_list_to_file():
  q = open('FileOfAppendedList','w')
  f = open('List2File', 'r')
  for i in f:
    q.write(get_page(i)+'\n')
  #print(type(f.read()))
  q.close()
  f.close()

#-------------zip the two list File of append list and list to file----
def zipit():
  q=open('List2File','r')
  q1 = q.readlines()
  r=open('FileOfAppendedList','r')
  r1 = r.readlines()
  d=open('Zipper','w') 
  #vb = [[x,y] for x in q for y in r if 'CA' in y] 
  #vb = [[x,y] for x in q1 for y in r1] 
  d1 = zip(q1,r1) 
  for h in d1:
    d.write(str(h)+'\n')
  q.close()
  r.close()
  d.close()

