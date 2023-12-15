from django import forms

#Source wattio/kg: https://www.bikeradar.com/advice/fitness-and-training/power-to-weight-ratio
class wattios_form (forms.Form):
    wattios_choices = [
    (6.2, 'Cyclist Exceptional'),
    (5.6, 'Cyclist Excelent'),
    (5, 'Cyclist Very Good'),
    (4.3, 'Cyclist Good'),
    (3.7, 'Cyclist Moderate'),
    (1.7, 'Cyclist Novice')
    ]

    wattios = forms.ChoiceField(choices=wattios_choices, widget=forms.Select(attrs={'id':'id_wattios_form'}))

class weight_form (forms.Form):
    weight_choices = [(x,x) for x in range (30,200, 5)]
    weight = forms.ChoiceField(choices=weight_choices, widget=forms.Select(attrs={'id':'id_weight_form'}))

class teeth_chainring_form (forms.Form):
    teeth_chainring_choices = [
            (87.5, '20T'),
            (91.55, '21T'),
            (95.6, '22T'),
            (99.65, '23T'),
            (103.7, '24T'),
            (107.75, '25T'),
            (111.8, '26T'),
            (115.85, '27T'),
            (119.9, '28T'),
            (123.95, '29T'),
            (128, '30T'),
            (132.05, '31T'),
            (136.1, '32T'),
            (140.15, '33T'),
            (144.2, '34T'),
            (148.2, '35T'),
            (152.2, '36T'),
            (156.25, '37T'),
            (160.3, '38T'),
            (164.35, '39T'),
            (168.4, '40T'),
            (172.45, '41T'),
            (176.5, '42T'),
            (180.55, '43T'),
            (184.6, '44T'),
            (188.65, '45T'),
            (192.7, '46T'),
            (196.75, '47T'),
            (200.8, '48T'),
            (204.8, '49T'),
            (208.8, '50T'),
            (212.85, '51T'),
            (216.9, '52T'),
            (220.95, '53T'),
            (225, '54T'),
            (229.05, '55T'),
            (233.1, '56T')  ]
    
    teeth_chainring = forms.ChoiceField(choices=teeth_chainring_choices, widget=forms.Select(attrs={'id':'id_teeth_chainring_form'}))

class teeth_2chainring_form (forms.Form):
    teeth_2chainring_choices = [
        ((42.95,  152.2),   '9T/36T'),
        ((42.95, 176.5),    '9T/42T'),
        ((47, 107.75),      '10T/25T'),
        ((47, 111.8),       '10T/26T'),
        ((47, 115.85),      '10T/27T'),
        ((47, 119.9),       '10T/28T')  
        ]
    teeth_2chainring = forms.ChoiceField(choices=teeth_2chainring_choices, widget=forms.Select(attrs={'id':'id_teeth_2chainring_form'}))

class teeth_cassette_form (forms.Form):
    teeth_cassette_choices = [
        ((42.95,  152.2),   '9T/36T'),
        ((42.95, 176.5),    '9T/42T'),
        ((47, 107.75),      '10T/25T'),
        ((47, 111.8),       '10T/26T'),
        ((47, 115.85),      '10T/27T'),
        ((47, 119.9),       '10T/28T'),
        ((47, 123.95),      '10T/29T'),
        ((47, 128.8),       '10T/30T'),
        ((47, 140.15),      '10T/33T'),
        ((47, 152.2),       '10T/36T'),
        ((47, 168.4),       '10T/40T'),
        ((47, 184.6),       '10T/44T'),
        ((47, 188.65),      '10T/45T'),
        ((47, 208.8),       '10T/50T'),
        ((47, 212.85),      '10T/51T'),
        ((51.05, 99.65),    '11T/23T'),
        ((51.05, 107.75),   '11T/25T'),
        ((51.05, 111.8),    '11T/26T'),
        ((51.05, 119.9),    '11T/28T'),
        ((51.05, 123.95),   '11T/29T'),
        ((51.05, 128),      '11T/30T'),
        ((51.05, 136.1),    '11T/32T'),
        ((51.05, 144.2),    '11T/34T'),
        ((51.05, 152.2),    '11T/36T'),
        ((51.05, 160.3),    '11T/38T'),
        ((51.05, 168.4),    '11T/40T'),
        ((51.05, 176.5),    '11T/42T'),
        ((51.05, 184.6),    '11T/44T'),
        ((51.05, 192.7),    '11T/46T'),
        ((51.05, 200.8),    '11T/48T'),
        ((51.05, 208.8),    '11T/50T'),
        ((51.05, 212.85),   '11T/51T'),
        ((55.1, 99.65),     '12T/23T'),
        ((55.1, 107.75),    '12T/25T'),
        ((55.1, 111.8),     '12T/26T'),
        ((55.1, 115.85),    '12T/27T'),
        ((55.1, 119.9),     '12T/28T'),
        ((55.1, 128),       '12T/30T'),
        ((55.1, 136.1),     '12T/32T'),
        ((55.1, 152.2),     '12T/36T'),
        ((55.1, 192.7),     '12T/46T')
    ]

    teeth_cassette = forms.ChoiceField(choices=teeth_cassette_choices, widget=forms.Select(attrs={'id':'id_teeth_cassette'}))