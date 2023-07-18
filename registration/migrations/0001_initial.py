# Generated by Django 4.1.2 on 2022-12-11 21:40

from django.db import migrations, models
import registration.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rider_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, validators=[registration.models.email_validation])),
                ('password', models.CharField(max_length=255)),
                ('password_repetition', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=75)),
                ('surname', models.CharField(max_length=75)),
                ('birth_date', models.DateField()),
                ('country', models.CharField(choices=[('Afghanistan\n', 'Afghanistan\n'), ('Albania\n', 'Albania\n'), ('Algeria\n', 'Algeria\n'), ('Andorra\n', 'Andorra\n'), ('Angola\n', 'Angola\n'), ('Antigua and Barbuda\n', 'Antigua and Barbuda\n'), ('Argentina\n', 'Argentina\n'), ('Armenia\n', 'Armenia\n'), ('Australia\n', 'Australia\n'), ('Austria\n', 'Austria\n'), ('Azerbaijan\n', 'Azerbaijan\n'), ('Bahamas\n', 'Bahamas\n'), ('Bahrain\n', 'Bahrain\n'), ('Bangladesh\n', 'Bangladesh\n'), ('Barbados\n', 'Barbados\n'), ('Belarus\n', 'Belarus\n'), ('Belgium\n', 'Belgium\n'), ('Belize\n', 'Belize\n'), ('Benin\n', 'Benin\n'), ('Bhutan\n', 'Bhutan\n'), ('Bolivia\n', 'Bolivia\n'), ('Bosnia and Herzegovina\n', 'Bosnia and Herzegovina\n'), ('Botswana\n', 'Botswana\n'), ('Brazil\n', 'Brazil\n'), ('Brunei\n', 'Brunei\n'), ('Bulgaria\n', 'Bulgaria\n'), ('Burkina Faso\n', 'Burkina Faso\n'), ('Burundi\n', 'Burundi\n'), ("CÃ´te d'Ivoire\n", "CÃ´te d'Ivoire\n"), ('Cabo Verde\n', 'Cabo Verde\n'), ('Cambodia\n', 'Cambodia\n'), ('Cameroon\n', 'Cameroon\n'), ('Canada\n', 'Canada\n'), ('Central African Republic\n', 'Central African Republic\n'), ('Chad\n', 'Chad\n'), ('Chile\n', 'Chile\n'), ('China\n', 'China\n'), ('Colombia\n', 'Colombia\n'), ('Comoros\n', 'Comoros\n'), ('Congo (Congo-Brazzaville)\n', 'Congo (Congo-Brazzaville)\n'), ('Costa Rica\n', 'Costa Rica\n'), ('Croatia\n', 'Croatia\n'), ('Cuba\n', 'Cuba\n'), ('Cyprus\n', 'Cyprus\n'), ('Czechia (Czech Republic)\n', 'Czechia (Czech Republic)\n'), ('Democratic Republic of the Congo\n', 'Democratic Republic of the Congo\n'), ('Denmark\n', 'Denmark\n'), ('Djibouti\n', 'Djibouti\n'), ('Dominica\n', 'Dominica\n'), ('Dominican Republic\n', 'Dominican Republic\n'), ('Ecuador\n', 'Ecuador\n'), ('Egypt\n', 'Egypt\n'), ('El Salvador\n', 'El Salvador\n'), ('Equatorial Guinea\n', 'Equatorial Guinea\n'), ('Eritrea\n', 'Eritrea\n'), ('Estonia\n', 'Estonia\n'), ('Eswatini (fmr. "Swaziland")\n', 'Eswatini (fmr. "Swaziland")\n'), ('Ethiopia\n', 'Ethiopia\n'), ('Fiji\n', 'Fiji\n'), ('Finland\n', 'Finland\n'), ('France\n', 'France\n'), ('Gabon\n', 'Gabon\n'), ('Gambia\n', 'Gambia\n'), ('Georgia\n', 'Georgia\n'), ('Germany\n', 'Germany\n'), ('Ghana\n', 'Ghana\n'), ('Greece\n', 'Greece\n'), ('Grenada\n', 'Grenada\n'), ('Guatemala\n', 'Guatemala\n'), ('Guinea\n', 'Guinea\n'), ('Guinea-Bissau\n', 'Guinea-Bissau\n'), ('Guyana\n', 'Guyana\n'), ('Haiti\n', 'Haiti\n'), ('Holy See\n', 'Holy See\n'), ('Honduras\n', 'Honduras\n'), ('Hungary\n', 'Hungary\n'), ('Iceland\n', 'Iceland\n'), ('India\n', 'India\n'), ('Indonesia\n', 'Indonesia\n'), ('Iran\n', 'Iran\n'), ('Iraq\n', 'Iraq\n'), ('Ireland\n', 'Ireland\n'), ('Israel\n', 'Israel\n'), ('Italy\n', 'Italy\n'), ('Jamaica\n', 'Jamaica\n'), ('Japan\n', 'Japan\n'), ('Jordan\n', 'Jordan\n'), ('Kazakhstan\n', 'Kazakhstan\n'), ('Kenya\n', 'Kenya\n'), ('Kiribati\n', 'Kiribati\n'), ('Kuwait\n', 'Kuwait\n'), ('Kyrgyzstan\n', 'Kyrgyzstan\n'), ('Laos\n', 'Laos\n'), ('Latvia\n', 'Latvia\n'), ('Lebanon\n', 'Lebanon\n'), ('Lesotho\n', 'Lesotho\n'), ('Liberia\n', 'Liberia\n'), ('Libya\n', 'Libya\n'), ('Liechtenstein\n', 'Liechtenstein\n'), ('Lithuania\n', 'Lithuania\n'), ('Luxembourg\n', 'Luxembourg\n'), ('Madagascar\n', 'Madagascar\n'), ('Malawi\n', 'Malawi\n'), ('Malaysia\n', 'Malaysia\n'), ('Maldives\n', 'Maldives\n'), ('Mali\n', 'Mali\n'), ('Malta\n', 'Malta\n'), ('Marshall Islands\n', 'Marshall Islands\n'), ('Mauritania\n', 'Mauritania\n'), ('Mauritius\n', 'Mauritius\n'), ('Mexico\n', 'Mexico\n'), ('Micronesia\n', 'Micronesia\n'), ('Moldova\n', 'Moldova\n'), ('Monaco\n', 'Monaco\n'), ('Mongolia\n', 'Mongolia\n'), ('Montenegro\n', 'Montenegro\n'), ('Morocco\n', 'Morocco\n'), ('Mozambique\n', 'Mozambique\n'), ('Myanmar (formerly Burma)\n', 'Myanmar (formerly Burma)\n'), ('Namibia\n', 'Namibia\n'), ('Nauru\n', 'Nauru\n'), ('Nepal\n', 'Nepal\n'), ('Netherlands\n', 'Netherlands\n'), ('New Zealand\n', 'New Zealand\n'), ('Nicaragua\n', 'Nicaragua\n'), ('Niger\n', 'Niger\n'), ('Nigeria\n', 'Nigeria\n'), ('North Korea\n', 'North Korea\n'), ('North Macedonia\n', 'North Macedonia\n'), ('Norway\n', 'Norway\n'), ('Oman\n', 'Oman\n'), ('Pakistan\n', 'Pakistan\n'), ('Palau\n', 'Palau\n'), ('Palestine State\n', 'Palestine State\n'), ('Panama\n', 'Panama\n'), ('Papua New Guinea\n', 'Papua New Guinea\n'), ('Paraguay\n', 'Paraguay\n'), ('Peru\n', 'Peru\n'), ('Philippines\n', 'Philippines\n'), ('Poland\n', 'Poland\n'), ('Portugal\n', 'Portugal\n'), ('Qatar\n', 'Qatar\n'), ('Romania\n', 'Romania\n'), ('Russia\n', 'Russia\n'), ('Rwanda\n', 'Rwanda\n'), ('Saint Kitts and Nevis\n', 'Saint Kitts and Nevis\n'), ('Saint Lucia\n', 'Saint Lucia\n'), ('Saint Vincent and the Grenadines\n', 'Saint Vincent and the Grenadines\n'), ('Samoa\n', 'Samoa\n'), ('San Marino\n', 'San Marino\n'), ('Sao Tome and Principe\n', 'Sao Tome and Principe\n'), ('Saudi Arabia\n', 'Saudi Arabia\n'), ('Senegal\n', 'Senegal\n'), ('Serbia\n', 'Serbia\n'), ('Seychelles\n', 'Seychelles\n'), ('Sierra Leone\n', 'Sierra Leone\n'), ('Singapore\n', 'Singapore\n'), ('Slovakia\n', 'Slovakia\n'), ('Slovenia\n', 'Slovenia\n'), ('Solomon Islands\n', 'Solomon Islands\n'), ('Somalia\n', 'Somalia\n'), ('South Africa\n', 'South Africa\n'), ('South Korea\n', 'South Korea\n'), ('South Sudan\n', 'South Sudan\n'), ('Spain\n', 'Spain\n'), ('Sri Lanka\n', 'Sri Lanka\n'), ('Sudan\n', 'Sudan\n'), ('Suriname\n', 'Suriname\n'), ('Sweden\n', 'Sweden\n'), ('Switzerland\n', 'Switzerland\n'), ('Syria\n', 'Syria\n'), ('Tajikistan\n', 'Tajikistan\n'), ('Tanzania\n', 'Tanzania\n'), ('Thailand\n', 'Thailand\n'), ('Timor-Leste\n', 'Timor-Leste\n'), ('Togo\n', 'Togo\n'), ('Tonga\n', 'Tonga\n'), ('Trinidad and Tobago\n', 'Trinidad and Tobago\n'), ('Tunisia\n', 'Tunisia\n'), ('Turkey\n', 'Turkey\n'), ('Turkmenistan\n', 'Turkmenistan\n'), ('Tuvalu\n', 'Tuvalu\n'), ('Uganda\n', 'Uganda\n'), ('Ukraine\n', 'Ukraine\n'), ('United Arab Emirates\n', 'United Arab Emirates\n'), ('United Kingdom\n', 'United Kingdom\n'), ('United States of America\n', 'United States of America\n'), ('Uruguay\n', 'Uruguay\n'), ('Uzbekistan\n', 'Uzbekistan\n'), ('Vanuatu\n', 'Vanuatu\n'), ('Venezuela\n', 'Venezuela\n'), ('Vietnam\n', 'Vietnam\n'), ('Yemen\n', 'Yemen\n'), ('Zambia\n', 'Zambia\n'), ('Zimbabwe\n', 'Zimbabwe\n')], max_length=33)),
                ('region', models.CharField(choices=[('Extremadura\n', 'Extremadura\n'), ('Castilla-La Mancha\n', 'Castilla-La Mancha\n'), ('Aragon\n', 'Aragon\n'), ('Castile and LeÃ³n\n', 'Castile and LeÃ³n\n'), ('Andalusia\n', 'Andalusia\n'), ('Castile-La Mancha\n', 'Castile-La Mancha\n'), ('Catalonia\n', 'Catalonia\n'), ('Murcia\n', 'Murcia\n'), ('Valencian Community\n', 'Valencian Community\n'), ('Asturias\n', 'Asturias\n'), ('Navarra\n', 'Navarra\n'), ('Galicia\n', 'Galicia\n'), ('Madrid\n', 'Madrid\n'), ('Cantabria\n', 'Cantabria\n'), ('La Rioja\n', 'La Rioja\n'), ('Balearic Islands\n', 'Balearic Islands\n'), ('Canary Islands\n', 'Canary Islands\n'), ('Basque Community\n', 'Basque Community\n'), ('Ceuta\n', 'Ceuta\n'), ('Melilla\n', 'Melilla\n')], max_length=20)),
                ('telephone', models.IntegerField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to=registration.models.upload_image_path)),
                ('bicycle_brand', models.CharField(max_length=75)),
                ('bicycle_model', models.CharField(max_length=75)),
                ('navigation_system', models.CharField(max_length=75)),
            ],
        ),
    ]
