from . import admin
from flask import Flask, render_template
import json

@admin.route('/product_list', methods=["GET"])
def product_list():
    return render_template('product_list.html')

@admin.route('/product_edit', methods=["GET","POST"])
def product_edit():
    return render_template('edit/product_edit.html')

@admin.route('/product_form')
def product_form():
    return render_template('form/product_form.html')