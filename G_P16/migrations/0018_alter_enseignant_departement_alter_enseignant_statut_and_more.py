# Generated by Django 4.2.5 on 2024-01-07 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('G_P16', '0017_alter_enseignant_statut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enseignant',
            name='Departement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='G_P16.departement', verbose_name='Département'),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='Statut',
            field=models.CharField(choices=[('missionnaire', 'Missionnaire'), ('vacataire', 'Vacataire'), ('titulaire', 'Titulaire')], max_length=15, verbose_name='Statut'),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='Departement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='G_P16.departement', verbose_name='Département'),
        ),
        migrations.AlterField(
            model_name='matiere',
            name='Departement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='G_P16.departement', verbose_name='Département'),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='Departement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='G_P16.departement', verbose_name='Département'),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='Droit',
            field=models.CharField(choices=[('second', 'Second'), ('admin', 'Admin')], max_length=20, verbose_name='Droit'),
        ),
    ]