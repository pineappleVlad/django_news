# Generated by Django 4.2.1 on 2023-05-27 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.CharField(max_length=10, verbose_name='Класс'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.CharField(max_length=10, verbose_name='Предмет'),
        ),
        migrations.CreateModel(
            name='TeacherStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teachers', models.ManyToManyField(related_name='Учителя', to='school.teacher')),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Учитель', to='school.teacherstudent'),
        ),
    ]
