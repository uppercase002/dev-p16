# Generated by Django 4.2.5 on 2024-01-07 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('G_P16', '0018_alter_enseignant_departement_alter_enseignant_statut_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enseignant',
            name='Statut',
            field=models.CharField(choices=[('vacataire', 'Vacataire'), ('missionnaire', 'Missionnaire'), ('titulaire', 'Titulaire')], max_length=15, verbose_name='Statut'),
        ),
        migrations.AlterField(
            model_name='matiere',
            name='Enseignant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='G_P16.enseignant', verbose_name='Enseignant'),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='Droit',
            field=models.CharField(choices=[('admin', 'Admin'), ('second', 'Second')], max_length=20, verbose_name='Droit'),
        ),
    ]