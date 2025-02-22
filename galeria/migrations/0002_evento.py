from django.db import migrations, models
class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('legenda', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('foto', models.CharField(max_length=150)),
            ],
        ),
    ]
