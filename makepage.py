#!/usr/bin/python
import os
import glob
import argparse
import ConfigParser

####################################################
# Utility functions
####################################################
def chunks(list_of_items, number_in_group):
    number_in_group = max(1, number_in_group)
    return (list_of_items[i:i+number_in_group] for i in xrange(0, len(list_of_items), number_in_group))

def load_config_data(filename):
    config = ConfigParser.ConfigParser()
    config.readfp(open(filename))

    return config 

def get_file_list(file_location):
    filelist = sorted(glob.glob(file_location + "/*.jpg"))
    return filelist

def inject_pagination(max_pages,cur_page=0):
    retval = '<ul class="pagination pagination-sm">'
    for x in range(0,max_pages):
        if cur_page == x:
            active = 'class="active"'
        else:
            active = ''
        retval  += '<li ' + active + '><a href="/index' + str(x) + '.html">' + str(x) + '</a></li>'
    retval += "</ul>"
    return retval

def outputPage(file_list,filename,cur_page,max_page):
    file_handle = open(filename + str(cur_page) + ".html",'w')
    #http://stackoverflow.com/questions/6773584/how-is-pythons-glob-glob-ordered
    file_handle.write("<html>")
    file_handle.write("<head>")
    #file_handle.write('<meta http-equiv="refresh" content="25" >')
    file_handle.write('<!-- Latest compiled and minified CSS -->')
    file_handle.write('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">')

    file_handle.write('<!-- jQuery library -->')
    file_handle.write('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>')

    file_handle.write('<!-- Latest compiled JavaScript -->')
    file_handle.write('<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>')

    file_handle.write('<link rel="stylesheet" type="text/css" href="css/style.css">')
    file_handle.write("</head>")
    file_handle.write("<body>")
    file_handle.write('<ul class="polaroids">')
    for file in file_list:
      locfile = file.split("html/")[1] 
      file_handle.write('<a href="' + locfile + '" title="' + locfile + '" >')
      file_handle.write('<li><img width="200px" src="' +  locfile + '"/></li>') 
      file_handle.write('</a>')
    file_handle.write('</ul>')
    file_handle.write(inject_pagination(max_page,cur_page)) 
    file_handle.write("</body>")
    file_handle.write("</html>")
    file_handle.close()

def main():
    parser = argparse.ArgumentParser(description='Generate Image web pages')
    parser.add_argument('--config',dest='configfile',help="Location of the configuration file",default="eagle_eye.config")
    args = parser.parse_args()
    if os.path.exists(args.configfile):
        config = load_config_data(args.configfile)
    else:
        print("Config file: %s doesn't exist" % args.configfile)
    file_location = config.get('main','file_location')
    pics_per_page = int(config.get('main','pic_per_page'))
     
    file_list = get_file_list(file_location)
    num_pages = len(file_list) / pics_per_page
    cur_page = 0
     
    for files  in chunks(file_list, pics_per_page):
        if cur_page < num_pages:
            outputPage(files,'/var/www/html/index', cur_page,num_pages)
            cur_page = cur_page + 1
         
if __name__ == "__main__":
    main()
