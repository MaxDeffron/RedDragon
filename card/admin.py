from django.contrib import admin
from .models import Category, Processor, Manufacturer, Memory, Сonnector, Power, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)


class ProcessorAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Processor, ProcessorAdmin)

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Manufacturer, ManufacturerAdmin)


class MemoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Memory, MemoryAdmin)

class СonnectorAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Сonnector, СonnectorAdmin)


class PowerAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Power, PowerAdmin)



class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created',
                    'updated', 'processor', 'hashrate', 'weight', 'lhr',
                    'manufacturer', 'memory', 'videomemory', 'frequency',
                    'cooler', 'image', 'description', 'power',
                    'connector', 'power', 'length', 'height', 'width',
                    'price_2', 'action', 'new']

    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)