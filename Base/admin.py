from django.contrib import admin

# Register your models here.
from django.contrib import admin
from Base.models import Contact
from Base.models import Project
from Base.models import Skill
from Base.models import Certification
from Base.models import About   


# Register your models here.
admin.site.register(Contact)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Certification)
admin.site.register(About)
