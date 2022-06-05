# Generated by Django 4.0.2 on 2022-06-02 04:28

from django.db import migrations
import mapbox_location_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0007_alter_somelocationmodel_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='somelocationmodel',
            name='location',
            field=mapbox_location_field.models.LocationField(map_attrs={'center': [17.031645, 51.106715], 'cursor_style': 'pointer', 'fullscreen_button': True, 'geocoder': True, 'language': 'auto', 'marker_color': 'blue', 'message_404': 'Dirección no definida', 'navigation_buttons': True, 'placeholder': 'Elija una ubicación en el mapa a continuación', 'readonly': True, 'rotate': False, 'style': 'mapbox://styles/mapbox/outdoors-v11', 'track_location_button': True, 'zoom': 1}),
        ),
    ]