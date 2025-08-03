from django.db import models
from django.contrib.auth.models import User

class BusinessType(models.Model):
    """
    Tipo de negocio, ej. taquería, ferretería.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class PostType(models.Model):
    """
    Tipo de publicación: frase, promoción, tip, anuncio.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Tone(models.Model):
    """
    Tono del post: divertido, profesional, urgente.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class GalleryImage(models.Model):
    """
    Imágenes prediseñadas para usar en posts.
    """
    name = models.CharField(max_length=100)
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    """
    Perfil de usuario con información de su negocio.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    business_name = models.CharField(max_length=255, blank=True)
    business_type = models.ForeignKey(BusinessType, blank=True, on_delete=models.SET_NULL, null=True)
    business_description = models.TextField(blank=True)
    content_goal = models.TextField(blank=True)  # Ej: "Promocionar productos", "Conectar con el cliente", etc.

    def __str__(self):
        return f"Perfil de {self.user.username}"

class UserPost(models.Model):
    """
    Post generado por el usuario con texto e imagen (propia o galería).
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    business_type = models.ForeignKey(BusinessType, on_delete=models.SET_NULL, null=True)
    post_type = models.ForeignKey(PostType, on_delete=models.SET_NULL, null=True)
    tone = models.ForeignKey(Tone, on_delete=models.SET_NULL, null=True)

    text = models.TextField()
    user_image_url = models.URLField(blank=True, null=True)
    gallery_image = models.ForeignKey(GalleryImage, on_delete=models.SET_NULL, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Post de {self.user.username} en {self.created_at.strftime('%Y-%m-%d %H:%M')}"

    @property
    def image(self):
        if self.user_image_url:
            return self.user_image_url
        elif self.gallery_image:
            return self.gallery_image.image_url
        return None
