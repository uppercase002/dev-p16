# Generated by Django 4.2.5 on 2023-12-31 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('G_P16', '0008_alter_enseignant_departement_alter_enseignant_statut_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enseignant',
            name='Departement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='G_P16.departement', verbose_name='Département'),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='Statut',
            field=models.CharField(choices=[('missionnaire', 'Missionnaire'), ('titulaire', 'Titulaire'), ('vacataire', 'Vacataire')], max_length=15, verbose_name='Statut'),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='Droit',
            field=models.CharField(choices=[('admin', 'Admin'), ('second', 'Second')], max_length=20, verbose_name='Droit'),
        ),
    ]
