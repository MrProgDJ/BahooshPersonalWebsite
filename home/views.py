from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import ContactMeForm
from .models import PersonalInfo, MySkill, Service, MyProject, SiteSetting, CertificatesOfAppreciation


class HomeView(TemplateView):
    template_name = 'home/home_page.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['personal_info'] = PersonalInfo.objects.filter(status=True).first()
        context['my_skills'] = MySkill.objects.filter(status=True)
        context['services'] = Service.objects.filter(status=True)
        context['my_projects'] = MyProject.objects.filter(status=True)
        context['certificates'] = CertificatesOfAppreciation.objects.filter(status=True)
        return context


class ContactMeView(CreateView):
    template_name = 'home/contact_me.html'
    form_class = ContactMeForm
    success_url = reverse_lazy('home_page')


class HeaderComponent(TemplateView):
    template_name = 'shared/header_component.html'

    def get_context_data(self, **kwargs):
        context = super(HeaderComponent, self).get_context_data(**kwargs)
        context['site_setting'] = SiteSetting.objects.filter(is_main_setting=True).first()
        return context


class FooterComponent(TemplateView):
    template_name = 'shared/footer_component.html'

    def get_context_data(self, **kwargs):
        context = super(FooterComponent, self).get_context_data(**kwargs)
        context['personal_info'] = PersonalInfo.objects.filter(status=True).first()
        context['site_setting'] = SiteSetting.objects.filter(is_main_setting=True).first()
        return context
