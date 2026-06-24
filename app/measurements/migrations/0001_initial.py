from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='MeasurementRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=120, verbose_name='Имя')),
                ('phone', models.CharField(max_length=30, verbose_name='Телефон')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('preferred_time', models.CharField(blank=True, max_length=120, verbose_name='Удобное время')),
                ('wishes', models.TextField(blank=True, verbose_name='Пожелания')),
                (
                    'status',
                    models.CharField(
                        choices=[
                            ('new', 'Новая'),
                            ('contacted', 'Связались'),
                            ('scheduled', 'Записана'),
                            ('done', 'Завершена'),
                        ],
                        default='new',
                        max_length=20,
                        verbose_name='Статус',
                    ),
                ),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
            ],
            options={
                'verbose_name': 'заявка на мерки',
                'verbose_name_plural': 'заявки на мерки',
                'ordering': ['-created_at'],
            },
        ),
    ]

