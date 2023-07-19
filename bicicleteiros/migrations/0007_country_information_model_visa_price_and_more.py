# Generated by Django 4.0.3 on 2023-07-19 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bicicleteiros', '0006_alter_country_information_model_time_zone'),
    ]

    operations = [
        migrations.AddField(
            model_name='country_information_model',
            name='visa_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='country_information_model',
            name='visa_requerided',
            field=models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=33, null=True),
        ),
        migrations.AlterField(
            model_name='country_information_model',
            name='time_zone',
            field=models.CharField(blank=True, choices=[['Africa/Abidjan', 'Africa/Abidjan'], ['Africa/Algiers', 'Africa/Algiers'], ['Africa/Bissau', 'Africa/Bissau'], ['Africa/Cairo', 'Africa/Cairo'], ['Africa/Casablanca', 'Africa/Casablanca'], ['Africa/Ceuta', 'Africa/Ceuta'], ['Africa/El_Aaiun', 'Africa/El_Aaiun'], ['Africa/Johannesburg', 'Africa/Johannesburg'], ['Africa/Juba', 'Africa/Juba'], ['Africa/Khartoum', 'Africa/Khartoum'], ['Africa/Lagos', 'Africa/Lagos'], ['Africa/Maputo', 'Africa/Maputo'], ['Africa/Monrovia', 'Africa/Monrovia'], ['Africa/Nairobi', 'Africa/Nairobi'], ['Africa/Ndjamena', 'Africa/Ndjamena'], ['Africa/Sao_Tome', 'Africa/Sao_Tome'], ['Africa/Tripoli', 'Africa/Tripoli'], ['Africa/Tunis', 'Africa/Tunis'], ['Africa/Windhoek', 'Africa/Windhoek'], ['America/Adak', 'America/Adak'], ['America/Anchorage', 'America/Anchorage'], ['America/Araguaina', 'America/Araguaina'], ['America/Argentina/Buenos_Aires', 'America/Argentina/Buenos_Aires'], ['America/Argentina/Catamarca', 'America/Argentina/Catamarca'], ['America/Argentina/Cordoba', 'America/Argentina/Cordoba'], ['America/Argentina/Jujuy', 'America/Argentina/Jujuy'], ['America/Argentina/La_Rioja', 'America/Argentina/La_Rioja'], ['America/Argentina/Mendoza', 'America/Argentina/Mendoza'], ['America/Argentina/Rio_Gallegos', 'America/Argentina/Rio_Gallegos'], ['America/Argentina/Salta', 'America/Argentina/Salta'], ['America/Argentina/San_Juan', 'America/Argentina/San_Juan'], ['America/Argentina/San_Luis', 'America/Argentina/San_Luis'], ['America/Argentina/Tucuman', 'America/Argentina/Tucuman'], ['America/Argentina/Ushuaia', 'America/Argentina/Ushuaia'], ['America/Asuncion', 'America/Asuncion'], ['America/Bahia', 'America/Bahia'], ['America/Bahia_Banderas', 'America/Bahia_Banderas'], ['America/Barbados', 'America/Barbados'], ['America/Belem', 'America/Belem'], ['America/Belize', 'America/Belize'], ['America/Boa_Vista', 'America/Boa_Vista'], ['America/Bogota', 'America/Bogota'], ['America/Boise', 'America/Boise'], ['America/Cambridge_Bay', 'America/Cambridge_Bay'], ['America/Campo_Grande', 'America/Campo_Grande'], ['America/Cancun', 'America/Cancun'], ['America/Caracas', 'America/Caracas'], ['America/Cayenne', 'America/Cayenne'], ['America/Chicago', 'America/Chicago'], ['America/Chihuahua', 'America/Chihuahua'], ['America/Ciudad_Juarez', 'America/Ciudad_Juarez'], ['America/Costa_Rica', 'America/Costa_Rica'], ['America/Cuiaba', 'America/Cuiaba'], ['America/Danmarkshavn', 'America/Danmarkshavn'], ['America/Dawson', 'America/Dawson'], ['America/Dawson_Creek', 'America/Dawson_Creek'], ['America/Denver', 'America/Denver'], ['America/Detroit', 'America/Detroit'], ['America/Edmonton', 'America/Edmonton'], ['America/Eirunepe', 'America/Eirunepe'], ['America/El_Salvador', 'America/El_Salvador'], ['America/Fort_Nelson', 'America/Fort_Nelson'], ['America/Fortaleza', 'America/Fortaleza'], ['America/Glace_Bay', 'America/Glace_Bay'], ['America/Goose_Bay', 'America/Goose_Bay'], ['America/Grand_Turk', 'America/Grand_Turk'], ['America/Guatemala', 'America/Guatemala'], ['America/Guayaquil', 'America/Guayaquil'], ['America/Guyana', 'America/Guyana'], ['America/Halifax', 'America/Halifax'], ['America/Havana', 'America/Havana'], ['America/Hermosillo', 'America/Hermosillo'], ['America/Indiana/Indianapolis', 'America/Indiana/Indianapolis'], ['America/Indiana/Knox', 'America/Indiana/Knox'], ['America/Indiana/Marengo', 'America/Indiana/Marengo'], ['America/Indiana/Petersburg', 'America/Indiana/Petersburg'], ['America/Indiana/Tell_City', 'America/Indiana/Tell_City'], ['America/Indiana/Vevay', 'America/Indiana/Vevay'], ['America/Indiana/Vincennes', 'America/Indiana/Vincennes'], ['America/Indiana/Winamac', 'America/Indiana/Winamac'], ['America/Inuvik', 'America/Inuvik'], ['America/Iqaluit', 'America/Iqaluit'], ['America/Jamaica', 'America/Jamaica'], ['America/Juneau', 'America/Juneau'], ['America/Kentucky/Louisville', 'America/Kentucky/Louisville'], ['America/Kentucky/Monticello', 'America/Kentucky/Monticello'], ['America/La_Paz', 'America/La_Paz'], ['America/Lima', 'America/Lima'], ['America/Los_Angeles', 'America/Los_Angeles'], ['America/Maceio', 'America/Maceio'], ['America/Managua', 'America/Managua'], ['America/Manaus', 'America/Manaus'], ['America/Martinique', 'America/Martinique'], ['America/Matamoros', 'America/Matamoros'], ['America/Mazatlan', 'America/Mazatlan'], ['America/Menominee', 'America/Menominee'], ['America/Merida', 'America/Merida'], ['America/Metlakatla', 'America/Metlakatla'], ['America/Mexico_City', 'America/Mexico_City'], ['America/Miquelon', 'America/Miquelon'], ['America/Moncton', 'America/Moncton'], ['America/Monterrey', 'America/Monterrey'], ['America/Montevideo', 'America/Montevideo'], ['America/New_York', 'America/New_York'], ['America/Nome', 'America/Nome'], ['America/Noronha', 'America/Noronha'], ['America/North_Dakota/Beulah', 'America/North_Dakota/Beulah'], ['America/North_Dakota/Center', 'America/North_Dakota/Center'], ['America/North_Dakota/New_Salem', 'America/North_Dakota/New_Salem'], ['America/Nuuk', 'America/Nuuk'], ['America/Ojinaga', 'America/Ojinaga'], ['America/Panama', 'America/Panama'], ['America/Paramaribo', 'America/Paramaribo'], ['America/Phoenix', 'America/Phoenix'], ['America/Port-au-Prince', 'America/Port-au-Prince'], ['America/Porto_Velho', 'America/Porto_Velho'], ['America/Puerto_Rico', 'America/Puerto_Rico'], ['America/Punta_Arenas', 'America/Punta_Arenas'], ['America/Rankin_Inlet', 'America/Rankin_Inlet'], ['America/Recife', 'America/Recife'], ['America/Regina', 'America/Regina'], ['America/Resolute', 'America/Resolute'], ['America/Rio_Branco', 'America/Rio_Branco'], ['America/Santarem', 'America/Santarem'], ['America/Santiago', 'America/Santiago'], ['America/Santo_Domingo', 'America/Santo_Domingo'], ['America/Sao_Paulo', 'America/Sao_Paulo'], ['America/Scoresbysund', 'America/Scoresbysund'], ['America/Sitka', 'America/Sitka'], ['America/St_Johns', 'America/St_Johns'], ['America/Swift_Current', 'America/Swift_Current'], ['America/Tegucigalpa', 'America/Tegucigalpa'], ['America/Thule', 'America/Thule'], ['America/Tijuana', 'America/Tijuana'], ['America/Toronto', 'America/Toronto'], ['America/Vancouver', 'America/Vancouver'], ['America/Whitehorse', 'America/Whitehorse'], ['America/Winnipeg', 'America/Winnipeg'], ['America/Yakutat', 'America/Yakutat'], ['Antarctica/Casey', 'Antarctica/Casey'], ['Antarctica/Davis', 'Antarctica/Davis'], ['Antarctica/Macquarie', 'Antarctica/Macquarie'], ['Antarctica/Mawson', 'Antarctica/Mawson'], ['Antarctica/Palmer', 'Antarctica/Palmer'], ['Antarctica/Rothera', 'Antarctica/Rothera'], ['Antarctica/Troll', 'Antarctica/Troll'], ['Asia/Almaty', 'Asia/Almaty'], ['Asia/Amman', 'Asia/Amman'], ['Asia/Anadyr', 'Asia/Anadyr'], ['Asia/Aqtau', 'Asia/Aqtau'], ['Asia/Aqtobe', 'Asia/Aqtobe'], ['Asia/Ashgabat', 'Asia/Ashgabat'], ['Asia/Atyrau', 'Asia/Atyrau'], ['Asia/Baghdad', 'Asia/Baghdad'], ['Asia/Baku', 'Asia/Baku'], ['Asia/Bangkok', 'Asia/Bangkok'], ['Asia/Barnaul', 'Asia/Barnaul'], ['Asia/Beirut', 'Asia/Beirut'], ['Asia/Bishkek', 'Asia/Bishkek'], ['Asia/Chita', 'Asia/Chita'], ['Asia/Choibalsan', 'Asia/Choibalsan'], ['Asia/Colombo', 'Asia/Colombo'], ['Asia/Damascus', 'Asia/Damascus'], ['Asia/Dhaka', 'Asia/Dhaka'], ['Asia/Dili', 'Asia/Dili'], ['Asia/Dubai', 'Asia/Dubai'], ['Asia/Dushanbe', 'Asia/Dushanbe'], ['Asia/Famagusta', 'Asia/Famagusta'], ['Asia/Gaza', 'Asia/Gaza'], ['Asia/Hebron', 'Asia/Hebron'], ['Asia/Ho_Chi_Minh', 'Asia/Ho_Chi_Minh'], ['Asia/Hong_Kong', 'Asia/Hong_Kong'], ['Asia/Hovd', 'Asia/Hovd'], ['Asia/Irkutsk', 'Asia/Irkutsk'], ['Asia/Jakarta', 'Asia/Jakarta'], ['Asia/Jayapura', 'Asia/Jayapura'], ['Asia/Jerusalem', 'Asia/Jerusalem'], ['Asia/Kabul', 'Asia/Kabul'], ['Asia/Kamchatka', 'Asia/Kamchatka'], ['Asia/Karachi', 'Asia/Karachi'], ['Asia/Kathmandu', 'Asia/Kathmandu'], ['Asia/Khandyga', 'Asia/Khandyga'], ['Asia/Kolkata', 'Asia/Kolkata'], ['Asia/Krasnoyarsk', 'Asia/Krasnoyarsk'], ['Asia/Kuching', 'Asia/Kuching'], ['Asia/Macau', 'Asia/Macau'], ['Asia/Magadan', 'Asia/Magadan'], ['Asia/Makassar', 'Asia/Makassar'], ['Asia/Manila', 'Asia/Manila'], ['Asia/Nicosia', 'Asia/Nicosia'], ['Asia/Novokuznetsk', 'Asia/Novokuznetsk'], ['Asia/Novosibirsk', 'Asia/Novosibirsk'], ['Asia/Omsk', 'Asia/Omsk'], ['Asia/Oral', 'Asia/Oral'], ['Asia/Pontianak', 'Asia/Pontianak'], ['Asia/Pyongyang', 'Asia/Pyongyang'], ['Asia/Qatar', 'Asia/Qatar'], ['Asia/Qostanay', 'Asia/Qostanay'], ['Asia/Qyzylorda', 'Asia/Qyzylorda'], ['Asia/Riyadh', 'Asia/Riyadh'], ['Asia/Sakhalin', 'Asia/Sakhalin'], ['Asia/Samarkand', 'Asia/Samarkand'], ['Asia/Seoul', 'Asia/Seoul'], ['Asia/Shanghai', 'Asia/Shanghai'], ['Asia/Singapore', 'Asia/Singapore'], ['Asia/Srednekolymsk', 'Asia/Srednekolymsk'], ['Asia/Taipei', 'Asia/Taipei'], ['Asia/Tashkent', 'Asia/Tashkent'], ['Asia/Tbilisi', 'Asia/Tbilisi'], ['Asia/Tehran', 'Asia/Tehran'], ['Asia/Thimphu', 'Asia/Thimphu'], ['Asia/Tokyo', 'Asia/Tokyo'], ['Asia/Tomsk', 'Asia/Tomsk'], ['Asia/Ulaanbaatar', 'Asia/Ulaanbaatar'], ['Asia/Urumqi', 'Asia/Urumqi'], ['Asia/Ust-Nera', 'Asia/Ust-Nera'], ['Asia/Vladivostok', 'Asia/Vladivostok'], ['Asia/Yakutsk', 'Asia/Yakutsk'], ['Asia/Yangon', 'Asia/Yangon'], ['Asia/Yekaterinburg', 'Asia/Yekaterinburg'], ['Asia/Yerevan', 'Asia/Yerevan'], ['Atlantic/Azores', 'Atlantic/Azores'], ['Atlantic/Bermuda', 'Atlantic/Bermuda'], ['Atlantic/Canary', 'Atlantic/Canary'], ['Atlantic/Cape_Verde', 'Atlantic/Cape_Verde'], ['Atlantic/Faroe', 'Atlantic/Faroe'], ['Atlantic/Madeira', 'Atlantic/Madeira'], ['Atlantic/South_Georgia', 'Atlantic/South_Georgia'], ['Atlantic/Stanley', 'Atlantic/Stanley'], ['Australia/Adelaide', 'Australia/Adelaide'], ['Australia/Brisbane', 'Australia/Brisbane'], ['Australia/Broken_Hill', 'Australia/Broken_Hill'], ['Australia/Darwin', 'Australia/Darwin'], ['Australia/Eucla', 'Australia/Eucla'], ['Australia/Hobart', 'Australia/Hobart'], ['Australia/Lindeman', 'Australia/Lindeman'], ['Australia/Lord_Howe', 'Australia/Lord_Howe'], ['Australia/Melbourne', 'Australia/Melbourne'], ['Australia/Perth', 'Australia/Perth'], ['Australia/Sydney', 'Australia/Sydney'], ['CET', 'CET'], ['CST6CDT', 'CST6CDT'], ['EET', 'EET'], ['EST', 'EST'], ['EST5EDT', 'EST5EDT'], ['Etc/GMT', 'Etc/GMT'], ['Etc/GMT-1', 'Etc/GMT-1'], ['Etc/GMT-10', 'Etc/GMT-10'], ['Etc/GMT-11', 'Etc/GMT-11'], ['Etc/GMT-12', 'Etc/GMT-12'], ['Etc/GMT-13', 'Etc/GMT-13'], ['Etc/GMT-14', 'Etc/GMT-14'], ['Etc/GMT-2', 'Etc/GMT-2'], ['Etc/GMT-3', 'Etc/GMT-3'], ['Etc/GMT-4', 'Etc/GMT-4'], ['Etc/GMT-5', 'Etc/GMT-5'], ['Etc/GMT-6', 'Etc/GMT-6'], ['Etc/GMT-7', 'Etc/GMT-7'], ['Etc/GMT-8', 'Etc/GMT-8'], ['Etc/GMT-9', 'Etc/GMT-9'], ['Etc/GMT+1', 'Etc/GMT+1'], ['Etc/GMT+10', 'Etc/GMT+10'], ['Etc/GMT+11', 'Etc/GMT+11'], ['Etc/GMT+12', 'Etc/GMT+12'], ['Etc/GMT+2', 'Etc/GMT+2'], ['Etc/GMT+3', 'Etc/GMT+3'], ['Etc/GMT+4', 'Etc/GMT+4'], ['Etc/GMT+5', 'Etc/GMT+5'], ['Etc/GMT+6', 'Etc/GMT+6'], ['Etc/GMT+7', 'Etc/GMT+7'], ['Etc/GMT+8', 'Etc/GMT+8'], ['Etc/GMT+9', 'Etc/GMT+9'], ['Etc/UTC', 'Etc/UTC'], ['Europe/Andorra', 'Europe/Andorra'], ['Europe/Astrakhan', 'Europe/Astrakhan'], ['Europe/Athens', 'Europe/Athens'], ['Europe/Belgrade', 'Europe/Belgrade'], ['Europe/Berlin', 'Europe/Berlin'], ['Europe/Brussels', 'Europe/Brussels'], ['Europe/Bucharest', 'Europe/Bucharest'], ['Europe/Budapest', 'Europe/Budapest'], ['Europe/Chisinau', 'Europe/Chisinau'], ['Europe/Dublin', 'Europe/Dublin'], ['Europe/Gibraltar', 'Europe/Gibraltar'], ['Europe/Helsinki', 'Europe/Helsinki'], ['Europe/Istanbul', 'Europe/Istanbul'], ['Europe/Kaliningrad', 'Europe/Kaliningrad'], ['Europe/Kirov', 'Europe/Kirov'], ['Europe/Kyiv', 'Europe/Kyiv'], ['Europe/Lisbon', 'Europe/Lisbon'], ['Europe/London', 'Europe/London'], ['Europe/Madrid', 'Europe/Madrid'], ['Europe/Malta', 'Europe/Malta'], ['Europe/Minsk', 'Europe/Minsk'], ['Europe/Moscow', 'Europe/Moscow'], ['Europe/Paris', 'Europe/Paris'], ['Europe/Prague', 'Europe/Prague'], ['Europe/Riga', 'Europe/Riga'], ['Europe/Rome', 'Europe/Rome'], ['Europe/Samara', 'Europe/Samara'], ['Europe/Saratov', 'Europe/Saratov'], ['Europe/Simferopol', 'Europe/Simferopol'], ['Europe/Sofia', 'Europe/Sofia'], ['Europe/Tallinn', 'Europe/Tallinn'], ['Europe/Tirane', 'Europe/Tirane'], ['Europe/Ulyanovsk', 'Europe/Ulyanovsk'], ['Europe/Vienna', 'Europe/Vienna'], ['Europe/Vilnius', 'Europe/Vilnius'], ['Europe/Volgograd', 'Europe/Volgograd'], ['Europe/Warsaw', 'Europe/Warsaw'], ['Europe/Zurich', 'Europe/Zurich'], ['HST', 'HST'], ['Indian/Chagos', 'Indian/Chagos'], ['Indian/Maldives', 'Indian/Maldives'], ['Indian/Mauritius', 'Indian/Mauritius'], ['MET', 'MET'], ['MST', 'MST'], ['MST7MDT', 'MST7MDT'], ['Pacific/Apia', 'Pacific/Apia'], ['Pacific/Auckland', 'Pacific/Auckland'], ['Pacific/Bougainville', 'Pacific/Bougainville'], ['Pacific/Chatham', 'Pacific/Chatham'], ['Pacific/Easter', 'Pacific/Easter'], ['Pacific/Efate', 'Pacific/Efate'], ['Pacific/Fakaofo', 'Pacific/Fakaofo'], ['Pacific/Fiji', 'Pacific/Fiji'], ['Pacific/Galapagos', 'Pacific/Galapagos'], ['Pacific/Gambier', 'Pacific/Gambier'], ['Pacific/Guadalcanal', 'Pacific/Guadalcanal'], ['Pacific/Guam', 'Pacific/Guam'], ['Pacific/Honolulu', 'Pacific/Honolulu'], ['Pacific/Kanton', 'Pacific/Kanton'], ['Pacific/Kiritimati', 'Pacific/Kiritimati'], ['Pacific/Kosrae', 'Pacific/Kosrae'], ['Pacific/Kwajalein', 'Pacific/Kwajalein'], ['Pacific/Marquesas', 'Pacific/Marquesas'], ['Pacific/Nauru', 'Pacific/Nauru'], ['Pacific/Niue', 'Pacific/Niue'], ['Pacific/Norfolk', 'Pacific/Norfolk'], ['Pacific/Noumea', 'Pacific/Noumea'], ['Pacific/Pago_Pago', 'Pacific/Pago_Pago'], ['Pacific/Palau', 'Pacific/Palau'], ['Pacific/Pitcairn', 'Pacific/Pitcairn'], ['Pacific/Port_Moresby', 'Pacific/Port_Moresby'], ['Pacific/Rarotonga', 'Pacific/Rarotonga'], ['Pacific/Tahiti', 'Pacific/Tahiti'], ['Pacific/Tarawa', 'Pacific/Tarawa'], ['Pacific/Tongatapu', 'Pacific/Tongatapu'], ['PST8PDT', 'PST8PDT'], ['WET', 'WET']], max_length=33, null=True),
        ),
    ]
