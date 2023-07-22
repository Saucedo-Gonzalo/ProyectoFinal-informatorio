from django.db import models
from apps.usuarios.models import Usuario

# Create your models here.
class Objetivo(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion= models.CharField(max_length=250,null=True,blank=True)
    imagen= models.ImageField(upload_to='noticias',null=True)
    estado = models.CharField(max_length=20,  default='habilitado', blank=True, null=True, db_comment='habiltado, deshabiliado')

    
    def __str__(self):
        return self.nombre
    
class Noticia(models.Model):
    titulo = models.CharField(max_length=120)
    creado = models.DateField(auto_now_add=True)
    cuerpo = models.TextField()
    autor= models.CharField(max_length=50, null=True, blank=True)
    imagen = models.ImageField(upload_to='noticias',null=True)
    objetivo=models.ForeignKey(Objetivo,on_delete=models.CASCADE,null=True)
    estado = models.CharField(max_length=20,  default='habilitado', blank=True, null=True, db_comment='habiltado, deshabiliado')
    
    def __str__(self):
        return self.titulo
    
    def TextCorto(self):
        return self.cuerpo[:180]+"..."
    
    def obtener_mis_comentarios(self):
        return self.mis_comentarios.all()
    
    def delete(self, *args, **kwargs):
        # Antes de eliminar la noticia, también eliminamos la imagen asociada (si existe)
        if self.imagen:
            self.imagen.delete()
        super().delete(*args, **kwargs)
       

class Comentario(models.Model):
	noticia = models.ForeignKey(Noticia, related_name = 'mis_comentarios', on_delete = models.CASCADE)
	texto = models.TextField()
	creado = models.DateTimeField(auto_now_add = True)
	usuario = models.ForeignKey(Usuario, related_name = 'usuario_comentario' , on_delete = models.CASCADE)

	def __str__(self):
		return self.texto
    