from django.contrib import admin

from index.models import page1


# Register your models here.
class myAdmin(admin.ModelAdmin):
    # fields = ('username', 'email')
    list_display = ('pk', 'about', 'nums_1', 'nums_2', 'nums_3', 'nums_4', 'service1',
                    'innovation', 'work')  # list
    search_fields = ('pk', 'username',)
    fieldsets = (
        ['Main', {
            'fields': ('about', 'service', 'innovation', 'work'),
        }],
        ['Advance', {
            'classes': ('collapse',),  # CSS
            'fields': ('nums_1', 'nums_2', 'nums_3', 'nums_4'),
        }]
    )


# admin.site.register(page1, myAdmin)
admin.site.register(page1)
