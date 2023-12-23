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

class groupset_brand_form (forms.Form):
    groupset_brand_choices = [
    ('Campagnolo', 'Campagnolo'),
    ('Shimano', 'Shimano'),
    ('Sram', 'Sram'),
    ('Microshift', 'Microshift'),
    ('State', 'State')
    ]
    groupset_brand = forms.ChoiceField(choices=groupset_brand_choices, widget=forms.Select(attrs={'id':'id_groupset_brand_form'}))

class groupset_model_form (forms.Form):
    groupset_model_choices = [
        ('Ekar', 'Ekar'),
        ('GRX', 'GRX'),
        ('Force eTap AXS (electronic)', 'Force eTap AXS (electronic)'),
        ('Force', 'Force'),
        ('Rival Etap AXS (electronic)', 'Rival Etap AXS (electronic)'),
        ('Rival', 'Rival'),
        ('Apex', 'Apex'),
        ('Sword', 'Sword'),
        ('All Road', 'All Road'),
        ('Super Record Wireless (electronic)', 'Super Record Wireless (electronic)'),
        ('Super Record', 'Super Record'),
        ('Record', 'Record'),
        ('Chorus', 'Chorus'),
        ('Dura-Ace (electronic)', 'Dura-Ace (electronic)'),
        ('Ultegra (electronic)', 'Ultegra (electronic)'),
        ('Shimano 105 (electronic)', 'Shimano 105 (electronic)'),
        ('Tiagra', 'Tiagra'),
        ('Sora', 'Sora'),
        ('Claris', 'Claris'),
        ('Red eTap AXS (electronic)', 'Red eTap AXS (electronic)'),
        ('XTR (electronic)', 'XTR (electronic)'),
        ('XTR', 'XTR'),
        ('Deore XT (electronic)', 'Deore XT (electronic)'),
        ('Deore', 'Deore'),
        ('SLX', 'SLX'),
        ('Cues', 'Cues'),
        ('Alivio', 'Alivio'),
        ('Acera', 'Acera'),
        ('Altus', 'Altus'),
        ('XX1 Eagle AXS (electronic)', 'XX1 Eagle AXS (electronic)'),
        ('XX1 Eagle', 'XX1 Eagle'),
        ('X01 Eagle AXS (electronic)', 'X01 Eagle AXS (electronic)'),
        ('X01 Eagle', 'X01 Eagle'),
        ('GX Eagle AXS (electronic)', 'GX Eagle AXS (electronic)'),
        ('GX Eagle', 'GX Eagle'),
        ('NX Eagle', 'NX Eagle'),
        ('SX Eagle', 'SX Eagle'),
        ('Advent X', 'Advent X'),
        ('Advent', 'Advent'),
        ('Acolyte', 'Acolyte')
    ]
    groupset_model = forms.ChoiceField(choices=groupset_model_choices, widget=forms.Select(attrs={'id':'id_groupset_model_form'}))

class teeth_1chainring_form (forms.Form):
    teeth_1chainring_choices = [
        (28,       '28T'),
        (30,       '30T'),
        (32,       '32T'),
        (33,       '33T'),
        (34,       '34T'),
        (35,       '35T'),
        (36,       '36T'),
        (38,       '38T'),
        (40,       '40T'),
        (42,       '42T'),
        (43,       '43T'),
        (44,       '44T'),
        (46,       '46T'),
        (48,       '48T'),
    ]

    teeth_1chainring = forms.ChoiceField(choices=teeth_1chainring_choices, widget=forms.Select(attrs={'id':'id_teeth_1chainring_form'}))

class teeth_2chainring_form (forms.Form):
    teeth_2chainring_choices = [
        ((36, 22),       '36T/22T'),
        ((36, 26),       '36T/26T'),
        ((38, 28),       '38T/28T'),
        ((43, 30),       '43T/30T'),
        ((45, 29),       '45T/29T'),
        ((46, 30),       '46T/30T'),
        ((46, 32),       '46T/32T'),
        ((46, 33),       '46T/33T'),
        ((46, 34),       '46T/34T'),
        ((48, 31),       '48T/31T'),
        ((48, 32),       '48T/32T'),
        ((48, 34),       '48T/34T'),
        ((48, 35),       '48T/35T'),
        ((46, 36),       '46T/36T'),
        ((50, 34),       '50T/34T'),
        ((50, 37),       '50T/37T'),
        ((52, 36),       '52T/36T'),
        ((52, 39),       '52T/39T'),
        ((53, 39),       '53T/39T'),
        ((54, 40),       '54T/40T'),
        ((54, 41),       '54T/41T'),
        ((56, 43),       '56T/43T'),
        ]
    teeth_2chainring = forms.ChoiceField(choices=teeth_2chainring_choices, widget=forms.Select(attrs={'id':'id_teeth_2chainring_form'}))

class teeth_3chainring_form (forms.Form):
    teeth_3chainring_choices = [
        ((40, 30, 22),       '40/30/22T'),
        ((44, 32, 22),       '44/32/22T'),
        ((59, 39, 30),       '59/39/30T'),
        ]
    teeth_3chainring = forms.ChoiceField(choices=teeth_3chainring_choices, widget=forms.Select(attrs={'id':'id_teeth_3chainring_form'}))

class teeth_cassette_form (forms.Form):
    teeth_cassette_choices = [
        ((9,10,11,12,13,14,16,18,20,23,27,31,36), '9T/36T'), #Ekar 13
        ((9,10,11,12,13,14,16,18,21,25,30,36,42), '9T/42T'), #Ekar 13
        ((),      '10T/25T'),
        ((),       '10T/26T'),
        ((),      '10T/27T'),
        ((),       '10T/28T'),
        ((),      '10T/29T'),
        ((),       '10T/30T'),
        ((),      '10T/33T'),
        ((),       '10T/36T'),
        ((10,11,12,13,14,15,17,20,23,27,32,38,44), '10T/44T'), #Ekar 13
        ((10,12,14,16,18,21,24,28,32,36,40,45),    '10T/45T'), #GRX 12
        ((),       '10T/50T'),
        ((10,12,14,16,18,21,24,28,33,39,45,51),    '10T/51T'), #GRX 12
        ((),      '10T/52T'),
        ((11,12,13,14,15,16,17,19,21,23,25),   '11T/25T'), #GRX 11
        ((11-12-13-14-15-17-19-21-23-25),       '11T/25T'), #GRX 10
        ((11,12,13,14,15,17,19,21,23,25,28),   '11T/28T'), #GRX 11
        ((),   '11T/29T'),
        ((11,12,13,14,15,16,17,19,21,24,27,30), '11T/30T'), #GRX 12
        ((11,12,13,14,15,17,19,21,24,27,30), '11T/30T'), #GRX 11
        ((11,12,13,14,16,18,20,22,25,28,32),    '11T/32T'), #GRX 11
        ((11,12,14,16,18,20,22,25,28,32),    '11T/32T'), #GRX 10
        ((11,12,13,14,15,17,19,21,24,27,30,34),    '11T/34T'), #GRX 12
        ((11,13,15,17,19,21,23,25,27,30,34),    '11T/34T'), #GRX 11
        ((11,13,15,17,19,21,23,26,30,34),    '11T/34T'), #GRX 10
        ((11,12,13,14,15,17,19,21,24,28,32,36),    '11T/36T'), #GRX 12
        ((11,13,15,17,19,21,24,28,32,36),    '11T/36T'), #GRX 10
        ((),    '11T/38T'),
        ((11,13,15,17,19,21,24,27,31,35,40),    '11T/40T'), #GRX 11
        ((11,13,15,17,19,21,24,28,32,37,42),    '11T/42T'), #GRX 11
        ((),    '11T/44T'),
        ((),    '11T/45T'),
        ((11,13,15,17,19,21,24,28,32,37,46),    '11T/46T'), #GRX 11
        ((),    '11T/48T'),
        ((),    '11T/50T'),
        ((),    '11T/51T'),
        ((12,13,14,15,16,17,18,19,21,23,25),  '12T/25T'), #GRX 11
        ((12,13,14,15,17,19,21,23,25,28),     '12T/28T'), #GRX 10
        ((),     '12T/36T'),
        ((),     '12T/42T'),
        ((),     '12T/46T'),
        ((),     '13T/25T'),
        ((),     '13T/26T'),
        ((14,15,16,17,18,19,20,21,23,25,28),     '14T/28T'), #GRX 11
        ((),     '14T/25T'),
    ]

    teeth_cassette = forms.ChoiceField(choices=teeth_cassette_choices, widget=forms.Select(attrs={'id':'id_teeth_cassette'}))