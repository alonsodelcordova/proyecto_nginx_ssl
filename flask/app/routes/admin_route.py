from flask import Blueprint, request, jsonify, render_template, session, redirect, flash
from app.models.user_model import User
from app.utils.decorators import session_required
from app.models.cliente_model import Cliente
from datetime import datetime
from app.models.producto_model import Product, Category
from app.models.factura_model import Factura, FacturaProducto
from flask import json

router_app = Blueprint('admin', __name__, url_prefix='/admin')


@router_app.get('/')
@session_required
def index_admin(current_user):
    return render_template('admin/index.html', current_user=current_user)

@router_app.get('/clientes')
@session_required
def clientes_get(current_user):
    clientes = Cliente.query.all()
    return render_template('admin/clientes.html', current_user=current_user, clientes=clientes)

@router_app.post('/clientes')
@session_required
def clientes_post(current_user):
    nombre = request.form.get('nombre')
    direccion = request.form.get('direccion')
    telefono = request.form.get('telefono')
    correo = request.form.get('correo')
    fecha_nacimiento = request.form.get('fecha_nacimiento')
    tipo = request.form.get('tipo')
    
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
    
    cliente = Cliente(nombre, direccion, telefono, correo, fecha_nacimiento, tipo)
    cliente.save()
    
    flash('Cliente creado exitosamente', 'success')
    return redirect('/admin/clientes')

@router_app.get('/clientes/<int:id>/eliminar')
@session_required
def clientes_delete(current_user, id):
    cliente = Cliente.query.get(id)
    if cliente is None:
        flash('Cliente no encontrado', 'danger')
        return redirect('/admin/clientes')
    
    if len(cliente.facturas) > 0:
        flash('El cliente no puede eliminarse porque tiene facturas asociadas', 'danger')
        return redirect('/admin/clientes')
    
    cliente.delete()
    flash('Cliente eliminado exitosamente', 'success')
    return redirect('/admin/clientes')


@router_app.get('/productos')
@session_required
def productos_get(current_user):
    productos = Product.query.all()
    categorias = Category.query.all()
    return render_template(
        'admin/productos.html', 
        current_user=current_user, 
        productos=productos,
        categorias=categorias
    )
    
@router_app.post('/productos')
@session_required
def productos_post(current_user):
    nombre = request.form.get('nombre')
    descripcion = request.form.get('descripcion')
    precio = request.form.get('precio')
    unidad = request.form.get('unidad')
    categoria = request.form.get('categoria')
    
    producto = Product(nombre, descripcion, precio, unidad, categoria)
    producto.save()
    flash('Producto creado exitosamente', 'success')
    return redirect('/admin/productos')

@router_app.get('/productos/<int:id>/eliminar')
@session_required
def productos_delete(current_user, id):
    producto = Product.query.get(id)
    if producto is None:
        flash('Producto no encontrado', 'danger')
        return redirect('/admin/productos')
    
    if len(producto.detalles) > 0:
        flash('El producto no puede eliminarse porque tiene facturas asociadas', 'danger')
        return redirect('/admin/productos')
    
    producto.delete()
    flash('Producto eliminado exitosamente', 'success')
    return redirect('/admin/productos')

@router_app.get('/facturas')
@session_required
def facturas_get(current_user):
    facturas = Factura.query.all()
    return render_template('admin/facturas/index.html', current_user=current_user, facturas=facturas)

@router_app.get('/facturas/nueva')
@session_required
def factura_nueva_get(current_user):
    clientes = Cliente.query.all()
    productos = Product.query.all()
    return render_template('admin/facturas/formulario.html', current_user=current_user, clientes=clientes, productos=productos)


@router_app.post('/facturas/nueva')
@session_required
def factura_nueva_post(current_user):
    cliente_id = request.form.get('cliente')
    fecha = request.form.get('fecha')
    subtotal = request.form.get('subtotal')
    total = request.form.get('total')
    productos = request.form.get('productos')
    
    fecha_date = datetime.strptime(fecha, '%Y-%m-%d')
    
    productos = json.loads(productos)
    
    cliente = Cliente.query.get(cliente_id)
    factura = Factura(cliente_id, fecha_date,subtotal, total)
    factura.save()
    
    for producto in productos:
        producto_id = producto.get('producto_id')
        cantidad = producto.get('cantidad')
        precio_unitario = producto.get('precio_unitario')
        
        factura_producto = FacturaProducto(producto_id, precio_unitario, cantidad)
        factura_producto.factura_id = factura.id
        factura_producto.save()
    flash('Factura creada exitosamente', 'success')
    return jsonify({'message': 'factura creada'})

@router_app.get('/facturas/<int:id>')
@session_required
def factura_detalle_get(current_user, id):
    factura = Factura.query.get(id)
    return render_template('admin/facturas/detalle_factura.html', current_user=current_user, factura=factura)

@router_app.get('/usuarios')
@session_required
def usuarios_get(current_user):
    usuarios = User.query.all()
    return render_template('admin/usuarios.html', current_user=current_user, usuarios=usuarios)

@router_app.get('/categorias')
@session_required
def categorias_get(current_user):
    categorias = Category.query.all()    
    return render_template('admin/categorias.html', current_user=current_user, categorias=categorias)

@router_app.post('/categorias')
@session_required
def categorias_post(current_user):
    nombre = request.form.get('nombre')
    
    categoria = Category(nombre)
    categoria.save()
    flash('Categoria creada exitosamente', 'success')
    return redirect('/admin/categorias')


@router_app.get('/categorias/<int:id>/eliminar')
@session_required
def categorias_delete(current_user, id):
    categoria = Category.query.get(id)
    if categoria is None:
        flash('Categoria no encontrada', 'danger')
        return redirect('/admin/categorias')
    
    
    if len(categoria.productos) > 0:
        flash('La categoria no puede eliminarse porque tiene productos asociados', 'danger')
        return redirect('/admin/categorias')
    
    categoria.delete()
    return redirect('/admin/categorias')
