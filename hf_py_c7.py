#!/usr/bin/env python3
#-*- coding:utf-8 -*-

# import pickle
# # from athletelist import AthleteList
#
# def get_coach_data(filename):
#
# def put_to_store(files_list):
#     all_athletes=()
#     for each_file in files_list:
#         ath=get_coach_data(each_file)
#         all_athletes[ath.name]=ath
#     try:
#         with open('athletes.pickle','wb') as athf:
#             pickle.dump(all_athletes,athf)
#     except  IOError as ioerr:
#         print('File error(put_and_store):'+str(ioerr))
#     return(all_athletes)
#
# def get_from_store():
#     all_athleles={}
#     try:
#         with open('athletes.pickle','rb') as athf:
#             all_athleles=pickle.load(athf)
#     except  IOError as ioerr:
#         print('File error(get_from_store):'+str(ioerr))
#     return(all_athleles)


from string import  Template

def start_response(resp="text/html"):
    return('Content-type; '+resp+'\n\n')

def include_header(the_title):
    whith open('templates/header.html') as headf
        head_text=headf.read()
    header=Template(head_text)
    return(header.substitude(title=the_title))

def include_footer(the_links):
    with open('tmeplates/footer.html') as footf:
        foot_text=footf.read()
    link_string=''
    for key in the_links:
        link_string+='<a href="'+the_links[key]+'">'+key+'</a>&nbsp;&nbsp;&nbsp;&nbsp;'
    footer=Template(foot_text)
    return(footer.substitute(links=link_string))

def start_form(the_url,form_type="POST"):
    return('<form action="'+the_url+'" method="'+form_type+'">')

def end_form(submit_msg="Submit"):
    return('<p></p><input type=submit value="'+submit_msg+'">')

def radio_button(rb_name,rb_value):
    return('<input type="radio"' name="'+rb_name+'" value="'+rb_value+'">'">'+rb_value+'<br />')
