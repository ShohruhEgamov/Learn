from django.contrib import admin
from .models import News,Category

# admin.site.register(News)
# admin.site.register(Category)

# Bu yerda qaysi narsalari ko'rinib turishi uchun
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','slug','publish_time','status') # Bu esa qaysilarni ko'rsatishi
    list_filter = ('status','created_time','publish_time') # Bu yerda filterlar nimaga ko'ra filterlashi
    prepopulated_fields = {'slug':('title',)} # Bu yerda titlega nima yozilsa slug ga ham avt shu yoziladi
    date_hierarchy = 'publish_time'
    search_fields = ('title','body') # Bu qidirish tizmi
    ordering = ('status','publish_time') # Tartiblash

@admin.register(Category) #Bu shart emas
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')

# admin.site.register(Category,CategoryAdmin)