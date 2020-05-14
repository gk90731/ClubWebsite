from django.contrib import admin
from appTwo.models import tech_team,org_team,Staff,Sudent_choice,final_result,notice_tech,notice_org,Post
# Register your models here.
admin.site.register(tech_team)
admin.site.register(org_team)
admin.site.register(Staff)
admin.site.register(Sudent_choice)
admin.site.register(final_result)
admin.site.register(notice_tech)
admin.site.register(notice_org)
admin.site.register(Post)

