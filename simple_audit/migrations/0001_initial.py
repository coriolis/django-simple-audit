# Generated by Django 2.0 on 2018-06-25 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Audit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('operation', models.PositiveIntegerField(choices=[(0, 'add'), (1, 'change'), (2, 'delete')], verbose_name='Operation')),
                ('object_id', models.PositiveIntegerField(db_index=True)),
                ('description', models.TextField()),
                ('obj_description', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Audit',
                'db_table': 'audit',
                'verbose_name_plural': 'Audits',
            },
        ),
        migrations.CreateModel(
            name='AuditChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=255)),
                ('old_value', models.TextField(blank=True, null=True)),
                ('new_value', models.TextField(blank=True, null=True)),
                ('audit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='field_changes', to='simple_audit.Audit')),
            ],
            options={
                'verbose_name': 'Audit',
                'db_table': 'audit_change',
                'verbose_name_plural': 'Audits',
            },
        ),
        migrations.CreateModel(
            name='AuditRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_id', models.CharField(max_length=255)),
                ('ip', models.GenericIPAddressField()),
                ('path', models.CharField(max_length=1024)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Audit',
                'db_table': 'audit_request',
                'verbose_name_plural': 'Audits',
            },
        ),
        migrations.AddField(
            model_name='audit',
            name='audit_request',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='simple_audit.AuditRequest'),
        ),
        migrations.AddField(
            model_name='audit',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
    ]
