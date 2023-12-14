from django import forms

class wattios_form (forms.Form):
    wattios_choices = [
    (4, 'Cyclist Pro'),
    (2, 'Cyclist middle'),
    (1, 'Cyclist Amateur'),
    ]

    wattios = forms.ChoiceField(choices=wattios_choices, widget=forms.Select(attrs={'id':'wattios_form'}))

class weight_form (forms.Form):
    weight_choices = [(x,x) for x in range (25,200, 5)]

    weight = forms.ChoiceField(choices=weight_choices, widget=forms.Select(attrs={'id':'weight_form'}))

class teeth_plate_form (forms.Form):
    teeth_plate_choices = [
            (38.9, '8T'),
            (42.95, '9T'),
            (47, '10T'),
            (51.05, '11T'),
            (55.1, '12T'),
            (59.15, '13T'),
            (63.2, '14T'),
            (67.25, '15T'),
            (71.3, '16T'),
            (75.35, '17T'),
            (79.4, '18T'),
            (83.45, '19T'),
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
            (216.9, '52T') ]
    
    teeth_plate = forms.ChoiceField(choices=teeth_plate_choices, widget=forms.Select(attrs={'id':'teeth_plate_form'}))

class teeth_cassette_form (forms.Form):
    teeth_cassette_choices = [
        ((47, 111.8), '10T/26T'),
        ((47, 119.9), '10T/28T'),
        ((47, 128.8), '10T/30T'),
        ((47, 140.15), '10T/33T'),
        ((47, 152.2), '10T/36T'),
        ((47, 184.6), '10T/44T'),
        ((47, 208.8), '10T/50T'),
        (4, '11T/23T'),
        (4, '11T/25T'),
        (4, '11T/26T'),
        (4, '11T/28T'),
        (4, '11T/30T'),
        (4, '11T/32T'),
        (4, '11T/34T'),
        (4, '11T/36T'),
        (4, '11T/42T'),
        (4, '11T/44T'),
        (4, '11T/50T'),
        (4, '12T/23T'),
        (4, '12T/25T'),
        (4, '12T/26T'),
        (4, '12T/27T'),
        (4, '12T/28T'),
        (4, '12T/32T'),
        (4, '12T/36T')

    ]

    teeth_cassette = forms.ChoiceField(choices=teeth_cassette_choices, widget=forms.Select(attrs={'id':'teeth_cassette'}))