from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_personalinfo_my_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='images/avatar', verbose_name='تصویر آواتار'),
        ),
    ]
