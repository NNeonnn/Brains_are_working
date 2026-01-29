#Выделенный файл для однострочных функций путей

from flask import render_template, request, redirect, url_for, send_file, session
from subscript.filework import *
from subscript.account_system import *

def landing():
    return render_template('landing.html', **commonkwargs(getlogin()))

def pricing():
    return render_template('pricing.html', **commonkwargs(getlogin()))

#def ultimate_dashboard():
#    return render_template('random_things/super_dashboard.html', **commonkwargs(getlogin()))

def rand(id):
    return render_template(f'random_things/rand{id}.html', **commonkwargs(getlogin()))