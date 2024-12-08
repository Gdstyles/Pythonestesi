from django.test import TestCase
from django.urls import reverse
from .models import Fabrica, Producto

# Create your tests here.
class ViewsTest(TestCase):
    
    def setUp(self):
        self.fabrica = Fabrica.objects.create(
            nombre='Fabrica', 
            pais='Chile'
            )
         
        self.producto = Producto.objects.create(
            nombre='Producto',
            precio=2000, 
            descripcion='descripcion', 
            fecha_vencimiento='2024-12-02',
            fabrica_id=self.fabrica.id
            )
    
    def test_listar_producto(self):
        response = self.client.get(reverse('listar'))
                         # recibimos,  esperamos
        print('response listar' ,response)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'Producto')
    
    def test_crear_producto(self):
        response = self.client.post(reverse('crear'), {
            'nombre':'Producto test para crear producto',
            'precio': 1500, 
            'descripcion': 'descripcion crear producto',
            'fecha_vencimiento': '2024-12-02',
            'fabrica_id': self.fabrica.id
        })
        
        print('response crear', response)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Producto.objects.count(),2)
        self.assertIsNotNone(response)
    
    def test_editar_producto(self):
        response = self.client.post(reverse('editar_producto', args=[self.producto.id]), {
            'nombre':'Producto test para editar producto',
            'precio': 1500, 
            'descripcion': 'descripcion editar producto',
            'fecha_vencimiento': '2024-12-02',
            'fabrica_id': self.fabrica.id
        })
        
        print('response editar ',response) 
        self.producto.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.producto.nombre, 'Producto test para editar producto')
        
    def test_eliminar_producto(self):
        producto = Producto.objects.create(
            nombre='Producto test para eliminar producto',
            precio=2000, 
            descripcion='descripcion eliminar producto', 
            fecha_vencimiento='2024-12-02',
            fabrica_id=self.fabrica.id
            )
        response = self.client.post(reverse('eliminar_producto', args=[producto.id]))
        
        print('response eliminar ',response)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Producto.objects.count(), 1)
        self.assertNotEqual(Producto.objects.count(), 2)
        
class ModelTest(TestCase):
    
    def setUp(self):
        self.fabrica = Fabrica.objects.create(
            nombre='Fabrica', 
            pais='Chile'
            )
         
        self.producto = Producto.objects.create(
            nombre='Producto',
            precio=2000, 
            descripcion='descripcion', 
            fecha_vencimiento='2024-12-02',
            fabrica_id=self.fabrica.id
            )
                
    def test_model_content_fabrica(self):
        self.assertEqual(self.fabrica.nombre, 'Fabrica')
        self.assertEqual(self.fabrica.pais, 'Chile')
        
    def test_model_content_producto(self):
        self.assertEqual(self.producto.nombre, 'Producto')
        self.assertEqual(self.producto.descripcion, 'descripcion')

class TemplateTest(TestCase):
    
    def setUp(self):
        self.fabrica = Fabrica.objects.create(
            nombre='Fabrica', 
            pais='Chile'
            )
         
        self.producto = Producto.objects.create(
            nombre='Producto',
            precio=2000, 
            descripcion='descripcion', 
            fecha_vencimiento='2024-12-02',
            fabrica_id=self.fabrica.id
            )
        
    def listar_productos(self):
        response = self.client.get(reverse('listar'))
        print('response listar template: ', response)
        
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listar')
        
    def test_crear_producto(self):
        response = self.client.get(reverse('crear'))
        print('response crear template' ,response)
        
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'crear_producto.html')

    def test_editar_producto(self):
        response = self.client.get(reverse('editar_producto', args=[self.producto.id]))
        print('response editar template' ,response)
        
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'editar_producto.html') 

        
    def test_buscar_producto(self):
        response = self.client.get(reverse('buscar'), {'query': 'Producto'})
        print('response buscar template')
        self.assertIsNotNone(response, 'listar_productos.html')
        
    def test_login(self):
        response = self.client.get(reverse('login'))
        print('response login template' , response)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        
    def test_logout(self):
        response = self.client.get(reverse('logout'))
        print('response logout template:', response) 
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        
    def test_registro(self):
        response = self.client.get(reverse('registro'))
        print('response registro template:', response) 
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registro.html')        
    
        