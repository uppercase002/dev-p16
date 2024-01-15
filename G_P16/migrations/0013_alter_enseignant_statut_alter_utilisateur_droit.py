# Generated by Django 4.2.5 on 2024-01-07 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('G_P16', '0012_etudiant_id_alter_enseignant_statut_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enseignant',
            name='Statut',
            field=models.CharField(choices=[('titulaire', 'Titulaire'), ('vacataire', 'Vacataire'), ('missionnaire', 'Missionnaire')], max_length=15, verbose_name='Statut'),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='Droit',
            field=models.CharField(choices=[('admin', 'Admin'), ('second', 'Second')], max_length=20, verbose_name='Droit'),
        ),
    ]