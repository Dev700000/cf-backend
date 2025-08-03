from django.contrib import admin
from .models import BusinessType, PostType, Tone, GalleryImage, UserPost, UserProfile

@admin.register(BusinessType)
class BusinessTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(PostType)
class PostTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Tone)
class ToneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image_url', 'created_at')
    search_fields = ('name',)

@admin.register(UserPost)
class UserPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'business_type', 'post_type', 'tone', 'created_at')
    list_filter = ('business_type', 'post_type', 'tone', 'created_at')
    search_fields = ('text', 'user__username')
    readonly_fields = ('created_at',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'image_preview')
    search_fields = ('user__username',)

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="50" height="50" style="object-fit:cover;" />'
        return "No image"
    image_preview.allow_tags = True
    image_preview.short_description = "Imagen"