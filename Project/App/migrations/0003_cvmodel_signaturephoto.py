# Generated by Django 4.0.6 on 2022-07-05 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_rename_fname_cvmodel_studentname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cvmodel',
            name='signaturePhoto',
            field=models.ImageField(default=None, upload_to='imgfolder'),
            preserve_default=False,
        ),
    ]