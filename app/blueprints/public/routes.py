from flask import render_template
from . import public_bp

@public_bp.route('/') # <--- Corregido: con comillas
def home():
    return render_template('public/home.html')

@public_bp.route('/tienda') # <--- Corregido: con slash inicial
def tienda():
    return render_template('public/tienda.html')

@public_bp.route('/contacto') # <--- Corregido: con slash inicial
def contacto():
    return render_template('public/contacto.html')