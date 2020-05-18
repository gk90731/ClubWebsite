from django.contrib import admin
from appTwo.models import tech_team,org_team,notice_tech,notice_org,Post,AptiTest,AptiStudent,AptiQuestion,AptiOption
# Register your models here.
admin.site.register(tech_team)
admin.site.register(org_team)
admin.site.register(notice_tech)
admin.site.register(notice_org)
admin.site.register(Post)
admin.site.register(AptiTest)
admin.site.register(AptiStudent)
admin.site.register(AptiQuestion)
admin.site.register(AptiOption)

