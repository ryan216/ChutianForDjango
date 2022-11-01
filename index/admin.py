import solve as solve
from django.contrib import admin


from index.models import page1, about, service, pm_con
from index.models import news


# Register your models here.
class myAdmin(admin.ModelAdmin):
    # fields = ('username', 'email')
    list_display = ('pk', 'about', 'nums_1', 'nums_2', 'nums_3', 'nums_4', 'service1',
                    'innovation1', 'work1')  # list
    search_fields = ('pk', 'username',)
    fieldsets = (
        ['Main', {
            'fields': ('about', 'service1', 'innovation1', 'work1'),
        }],
        ['Advance', {
            'classes': ('collapse',),  # CSS
            'fields': ('nums_1', 'nums_2', 'nums_3', 'nums_4'),
        }]
    )


# admin.site.register(page1, myAdmin)
admin.site.register(page1)
admin.site.register(news)
admin.site.register(about)
admin.site.register(service)
admin.site.register(pm_con)

