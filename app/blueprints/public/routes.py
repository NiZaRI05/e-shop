from flask import render_template
from . import public_bp

@public_bp.route('/') 
def home():
    return render_template('auth/home.html')

@public_bp.route('/tienda') 
def tienda():
    return render_template('auth/tienda.html')

@public_bp.route('/contacto') 
def contacto():
    return render_template('auth/contacto.html')