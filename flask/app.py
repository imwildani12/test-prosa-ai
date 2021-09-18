  
from flask import Flask, render_template, request, redirect, url_for, session


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')