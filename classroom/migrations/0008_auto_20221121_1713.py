# Generated by Django 3.0.4 on 2022-11-21 16:13

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0007_auto_20210402_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='Passage',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='Passage',
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_image',
            field=models.ImageField(default='None', upload_to='anwerimages'),
        ),
        migrations.AddField(
            model_name='question',
            name='passage',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='question_image',
            field=models.ImageField(default='None', upload_to='questionimages'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='passage',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.TextField(max_length=255, verbose_name='Answer'),
        ),
    ]
