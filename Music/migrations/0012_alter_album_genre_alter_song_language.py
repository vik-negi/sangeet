# Generated by Django 4.0.4 on 2023-07-19 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0011_alter_album_genre_alter_song_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.CharField(choices=[('Metal', 'Metal'), ('Hollywood', 'Hollywood'), ('Classical', 'Classical'), ('Pop Music', 'Pop Music'), ('Rock', 'Rock'), ('Hip Hop and Rap', 'Hip Hop and Rap'), ('K-POP', 'K-POP'), ('Folk', 'Folk'), ('Bollywood', 'Bollywood'), ('Techno', 'Techno')], max_length=200),
        ),
        migrations.AlterField(
            model_name='song',
            name='language',
            field=models.CharField(choices=[('Kumaoni', 'Kumaoni'), ('English', 'English'), ('Hindi', 'Hindi'), ('korean', 'korean'), ('Punjabi', 'Punjabi')], max_length=200),
        ),
    ]
