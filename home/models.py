from django.db import models


class MyProject(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    image = models.ImageField(upload_to='images/projects', null=True, blank=True, verbose_name='تصویر پروژه')
    description = models.TextField(verbose_name='توضیحات پروژه')
    link = models.URLField(verbose_name='آدرس پروژه', null=True, blank=True)
    status = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'پروژه من'
        verbose_name_plural = 'پروژه های من'


class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="نام")
    last_name = models.CharField(max_length=100, verbose_name="نام خانوادگی")
    avatar = models.ImageField(upload_to='images/avatar', verbose_name='تصویر آواتار', null=True, blank=True)
    job_position = models.CharField(max_length=100, verbose_name="سمت شغلی")
    about_me_text = models.TextField(verbose_name='درباره من')
    my_resume = models.FileField(upload_to='files/my_resume', verbose_name='رزومه من', null=True, blank=True)
    phone_number = models.CharField(max_length=15, verbose_name='تلفن همراه', null=True, blank=True)
    instagram = models.URLField(verbose_name='اینستاگرام', null=True, blank=True)
    telegram = models.URLField(verbose_name='تلگرام', null=True, blank=True)
    github = models.URLField(verbose_name='گیتهاب', null=True, blank=True)
    linkedin = models.URLField(verbose_name='لینکدین', null=True, blank=True)
    status = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    def __str__(self):
        return f'{self.last_name} - {self.job_position}'

    class Meta:
        verbose_name = 'اطلاعات شخصی من'
        verbose_name_plural = 'اطلاعات های شخصی من'


class MySkill(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان مهارت')
    progress_value = models.IntegerField(verbose_name='درصد')
    progress_width = models.IntegerField(verbose_name='عرض')
    status = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مهارت من'
        verbose_name_plural = 'مهارت های من'


class CertificatesOfAppreciation(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان تقدیرنامه', null=True, blank=True)
    image = models.ImageField(upload_to='images/certifications', verbose_name='تقدیرنامه ها')
    status = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تقدیر نامه'
        verbose_name_plural = 'تقدیر نامه ها'


class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان سرویس')
    image = models.FileField(upload_to='images/offer', verbose_name='تصویر')
    description = models.TextField(verbose_name='توضیحات')
    status = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'سرویس'
        verbose_name_plural = 'سرویس ها'


class SiteSetting(models.Model):
    site_name = models.CharField(max_length=100, verbose_name='نام سایت')
    site_url = models.CharField(max_length=100, verbose_name='آدرس سایت')
    site_logo = models.ImageField(upload_to="images/site_logo", null=True, blank=True, verbose_name='لوگو سایت')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='آدرس')
    copy_right = models.TextField(max_length=500, verbose_name='متن کپی رایت')
    is_main_setting = models.BooleanField(default=False, verbose_name='تنظیمات اصلی')

    def __str__(self):
        return f"{self.site_name} - {self.site_url}"

    class Meta:
        verbose_name = 'تنظیم سایت'
        verbose_name_plural = 'تنظیمات سایت'


class ContactMeModel(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    subject = models.CharField(max_length=100, verbose_name='موضوع')
    body = models.TextField(verbose_name='متن پیام')
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')

    def __str__(self):
        return f'{self.email} - {self.subject}'

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'
