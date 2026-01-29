#Выделенный файл для всех путей, связанных со страницей товаров

from flask import render_template, request, redirect, url_for, send_file, session
from subscript.filework import *
from subscript.account_system import *

def set_admin_query():
    email = getlogin()
    user = getuser(email)
    if email == 'placeholder' or user['rights'] != 3:
        return redirect(url_for('login'))
    data = request.form.to_dict(flat=False)
    qu = getquerylist("povar_to_admin.json")
    for i in range(len(qu)):
        if (qu[i]['id'] == int(data['id'][0])):
            qu[i]['status'] = int(data['result'][0])
            break
    setquerylist(name="povar_to_admin.json", to=qu)
    return redirect(url_for('dashboard'), 302)

def send_global():
    email = getlogin()
    user = getuser(email)
    if (email == 'placeholder' or user['rights'] != 3):
        return redirect(url_for('login'), 302)
    return render_template('send_global.html', tovarlist=gettovarlist(), **commonkwargs(email))

def send_global_file():
    email = getlogin()
    user = getuser(email)
    if (email == 'placeholder' or user['rights'] != 3):
        return redirect(url_for('login'), 302)
    if (request.method == 'POST'):
        data = request.form.to_dict(flat=False)
        if (data['commit_type'][0] == 'update_global'):
            txt = request.files['global_menu']
            if (txt.filename != ''):
                path = f"{base_path}/tovars/global_menu.txt"
                txt.save(path)
                f = parse_menu_txt()
                setglobtovarlist(f[0])
                setcats(f[1])
    return redirect(url_for('send_global'), 302)
