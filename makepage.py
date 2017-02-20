#!/usr/bin/python
import glob
#http://stackoverflow.com/questions/6773584/how-is-pythons-glob-glob-ordered
filelist = sorted(glob.glob("/var/www/html/pics/*.jpg"))
print("<html>")
print("<head>")
#print('<meta http-equiv="refresh" content="25" >')
print('<link rel="stylesheet" type="text/css" href="css/style.css">')
print("</head>")
print("<body>")
print('<ul class="polaroids">')
for file in filelist:
  locfile = file.split("html/")[1] 
  print('<a href="' + locfile + '" title="' + locfile + '" >')
  print('<li><img width="200px" src="' +  locfile + '"/></li>') 
  print('</a>')
print('</ul>')
print("</body>")
print("</html>")
