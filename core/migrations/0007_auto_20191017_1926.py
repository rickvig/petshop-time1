# Generated by Django 2.2.4 on 2019-10-17 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_servico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('uf', models.CharField(max_length=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='contato',
        ),
        migrations.RemoveField(
            model_name='fornecedor',
            name='contato',
        ),
        migrations.AlterField(
            model_name='produto',
            name='unidade_medida',
            field=models.CharField(choices=[('kg', 'Kg'), ('un', 'Un')], default='Un', max_length=5),
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=20)),
                ('descricao', models.CharField(choices=[('Fixo', 'Fixo'), ('Celular', 'Celular')], default='Celular', max_length=80)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Cliente')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Fornecedor')),
            ],
        ),
        migrations.CreateModel(
            name='Raca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('especie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Especie')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=100)),
                ('cep', models.CharField(blank=True, max_length=8, null=True)),
                ('numero', models.IntegerField()),
                ('complemetno', models.CharField(blank=True, max_length=100, null=True)),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Cidade')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Cliente')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Fornecedor')),
            ],
        ),
        migrations.AddField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Estado'),
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cor', models.CharField(max_length=50)),
                ('data_nascimento', models.DateField()),
                ('sexo', models.CharField(choices=[('M', 'Macho'), ('F', 'Fêmea')], max_length=5)),
                ('dono', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Cliente')),
                ('raca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Raca')),
            ],
        ),
    ]