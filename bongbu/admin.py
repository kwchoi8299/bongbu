from django.contrib import admin
from .models import Question, Realty_News, Realty_News_Comment

# admin.site.register(Question)
# admin.site.register(Realty_News)
# admin.site.register(Realty_News_Comment)

class QuestionAdmin(admin.ModelAdmin):
    # 리스트에서 보일 필드들
    list_display = ['subject', 'create_date']
    
    # 필터 사용
    list_filter = ['create_date']
    
    # 검색 기능 사용
    search_fields = ['subject']

class NewsAdmin(admin.ModelAdmin):
    # 리스트에서 보일 필드들
    list_display = ['title', 'create_date']
    
    # 필터 사용
    list_filter = ['create_date']
    
    # 검색 기능 사용
    search_fields = ['title']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Realty_News, NewsAdmin)