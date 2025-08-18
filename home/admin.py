from django.contrib import admin
from .models import PersonalInfo, MySkill, CertificatesOfAppreciation, Service, MyProject, SiteSetting, ContactMeModel

admin.site.register(MyProject)
admin.site.register(PersonalInfo)
admin.site.register(MySkill)
admin.site.register(CertificatesOfAppreciation)
admin.site.register(Service)
admin.site.register(SiteSetting)
admin.site.register(ContactMeModel)
