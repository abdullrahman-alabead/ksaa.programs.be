# Generated by Django 3.1.4 on 2024-08-25 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_auto_20240805_1131'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AppsPageData',
        ),
        migrations.RemoveField(
            model_name='headerlink',
            name='global_data',
        ),
        migrations.RemoveField(
            model_name='industry',
            name='homepage',
        ),
        migrations.RemoveField(
            model_name='quality',
            name='homepage',
        ),
        migrations.RemoveField(
            model_name='service',
            name='homepage',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='homepage',
        ),
        migrations.RemoveField(
            model_name='value',
            name='homepage',
        ),
        migrations.RemoveField(
            model_name='videodata',
            name='apps_page',
        ),
        migrations.DeleteModel(
            name='ApplicationCategory',
        ),
        migrations.DeleteModel(
            name='GlobalData',
        ),
        migrations.DeleteModel(
            name='HeaderLink',
        ),
        migrations.DeleteModel(
            name='HomepageData',
        ),
        migrations.DeleteModel(
            name='Industry',
        ),
        migrations.DeleteModel(
            name='Quality',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.DeleteModel(
            name='Solution',
        ),
        migrations.DeleteModel(
            name='Value',
        ),
        migrations.DeleteModel(
            name='VideoData',
        ),
    ]
