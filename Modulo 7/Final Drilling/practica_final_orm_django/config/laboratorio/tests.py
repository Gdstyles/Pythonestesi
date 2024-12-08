from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio, DirectorGeneral, Producto
# Create your tests here.


class ViewsTest(TestCase):
    
    def setUp(self):
        self.laboratorio = Laboratorio.objects.create(
        nombre='Laboratorio',
        ciudad='Santiago',
        pais='Chile'
    )
        
    def test1(self):
        
        laboratorio = Laboratorio.objects.get(id=self.laboratorio.id)
        self.assertEqual(laboratorio.nombre, "Laboratorio")
        self.assertEqual(laboratorio.ciudad, "Santiago")
        self.assertEqual(laboratorio.pais, 'Chile')    
    
    def test_laboratorio(self):
        
        response = self.client.get(reverse('listar_laboratorios'))
        
        self.assertEqual(response.status_code, 200)
        
        
    def test_laboratorio_http(self):
        
        response = self.client.get(reverse('listar_laboratorios'))
                 
        self.assertEqual(response.status_code, 200)
        
        self.assertTemplateUsed(response, 'listar_laboratorios.html')
        self.assertContains(response, "Laboratorio")
        self.assertContains(response, "Santiago")
        self.assertContains(response, "Chile")
        