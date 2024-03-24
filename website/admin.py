from django.contrib import admin

from .models import JobSeeker,Qualification,Position, Contact,Vacancy,Service,Point,JobPost,TimeSheet


admin.site.register(JobSeeker)
admin.site.register(Qualification)
admin.site.register(Position)
admin.site.register(Contact)
admin.site.register(Vacancy)
admin.site.register(Service)
admin.site.register(Point)
admin.site.register(JobPost)
admin.site.register(TimeSheet)