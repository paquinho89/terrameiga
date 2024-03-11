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
        ('Shimano 105', 'Shimano 105'),
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

class teeth_chainring_form (forms.Form):
    teeth_chainring_choices = [
        ('28',           '28T'),
        ('30',           '30T'),
        ('32',           '32T'),
        ('33',           '33T'),
        ('34',           '34T'),
        ('35',           '35T'),
        ('36',           '36T'),
        ('22-36',     '36T-22T'),
        ('26-36',     '36T-26T'),
        ('38',           '38T'),
        ('28-38',     '38T-28T'),
        ('40',           '40T'),
        ('22-30-40', '40-30-22T'),
        ('42',           '42T'),
        ('43',           '43T'),
        ('30-43',     '43T-30T'),
        ('44',           '44T'),
        ('22-32-44', '44-32-22T'),
        ('29-45',     '45T-29T'),
        ('46',           '46T'),
        ('30-46',     '46T-30T'),
        ('32-46',     '43T-32T'),
        ('33-46',     '46T-33T'),
        ('34-46',     '46T-34T'),
        ('36-46',     '46T-36T'),
        ('48',           '48T'),
        ('31-48',     '48T-31T'),
        ('32-48',     '48T-32T'),
        ('34-48',     '48T-34T'),
        ('35-48',     '48T-35T'),
        ('50-34',     '50T-34T'),
        ('37-50',     '50T-37T'),
        ('36-52',     '52T-36T'),
        ('39-52',     '52T-39T'),
        ('39-53',     '53T-39T'),
        ('40-54',     '54T-40T'),
        ('41-54',     '41T-54T'),
        ('43-56',     '56T-43T'),
        ('30-39-59', '59T-39T-30T')
    ]

    teeth_chainring = forms.ChoiceField(choices=teeth_chainring_choices, widget=forms.Select(attrs={'id':'id_teeth_chainring_form'}))

class teeth_cassette_form (forms.Form):
    teeth_cassette_choices = [
        ('36-31-27-23-20-18-16-14-13-12-11-10-9', '9T-36T - 13 speeds'), #Ekar 13
        ('42-36-30-25-21-18-16-14-13-12-11-10-9', '9T-42T - 13 speeds'),  #Ekar 13
        ('25-23-21-19-17-16-15-14-13-12-11-10',   '10T-25T - 12 speeds'), #Super Record Wireless 12
        ('26-23-21-19-17-16-15-14-13-12-11-10',   '10T-26T - 12 speeds'), #RED eTap AXS 12
        ('27-24-21-19-17-16-15-14-13-12-11-10',   '10T-27T - 12 speeds'), #Super Record Wireless 12
        ('28-24-21-19-17-16-15-14-13-12-11-10',   '10T-28T - 12 speeds'), #Force eTap AXS (electronic) 12 #Force 12 #RED eTap AXS 12
        ('29-26-23-20-18-16-15-14-13-12-11-10',   '10T-29T - 12 speeds'), #Super Record Wireless 12
        ('30-27-24-21-19-17-15-14-13-12-11-10',   '10T-30T - 12 speeds'), #Force eTap AXS (electronic) 12 #Force 12 #Rival eTap AXS (electronic) 12 #Rival 12
        ('33-28-24-21-19-17-15-14-13-12-11-10',   '10T-33T - 12 speeds'), #Force eTap AXS (electronic) 12 #Force 12 #RED eTap AXS 12
        ('36-32-28-24-21-19-17-15-13-12-11-10',   '10T-36T - 12 speeds'), #Force eTap AXS (electronic) 12 #Force 12 #Rival eTap AXS (electronic) 12 #Rival 12
        ('44-38-32-28-24-21-19-17-15-13-11-10',   '10T-44T - 12 speeds'), #Force eTap AXS (electronic) 12 #Force 12 #Rival eTap AXS (electronic) 12 #Rival 12 #RED eTap AXS 12
        ('44-38-32-27-23-20-17-15-14-13-12-11-10','10T-44T - 13 speeds'), #Ekar 13
        ('45-40-36-32-28-24-21-18-16-14-12-10',   '10T-45T - 12 speeds'), #GRX 12 #SLX 12 #XTR electronic 12 #XTR 12 #Deore XT electronic 12 #Deore XT 12
        ('50-42-36-32-28-24-21-18-16-14-12-10',   '10T-50T - 12 speeds'), #XX1 Eagle AXS (electronic) 12 #X01 Eagle AXS (electronic) 12 
        ('51-45-39-33-28-24-21-18-16-14-12-10',   '10T-51T - 12 speeds'), #GRX 12 #Deore 12 #SLX 12 #XTR electronic 12 #XTR 12 #Deore XT electronic 12 #Deore XT 
        ('52-42-36-32-28-24-21-18-16-14-12-10',   '10T-52T - 12 speeds'), #GX Eagle electronic 12 #GX Eagle 12 # XX1 Eagle 12 #X01 Eagle AXS (electronic) 12 #X01 Eagle 12
        ('25-23-21-19-17-15-13-12-11',            '11T-25T - 9 speeds'), #Alivio 9 #Acera 9
        ('25-23-21-19-17-15-14-13-12-11',         '11T-25T - 10 speeds'), #GRX 10 #Tiagra 10
        ('25-23-21-19-17-16-15-14-13-12-11',      '11T-25T - 11 speeds'), #GRX 11
        ('28-24-21-19-17-15-13-11',               '11T-28T - 8 speeds'), #Claris 8
        ('28-25-23-21-19-17-15-14-13-12-11',      '11T-28T - 11 speeds'), #GRX 11
        ('29-26-23-21-19-17-16-15-14-13-12-11',   '11T-29T - 12 speeds'), #Chorus 12 #Super Record 12 #Record 12
        ('30-26-23-20-17-15-13-11',               '11T-30T - 8 speeds'), #Claris 8
        ('30-26-23-20-18-16-14-12-11',            '11T-30T - 9 speeds'), #Sora 9
        ('30-27-24-21-19-17-15-14-13-12-11',      '11T-30T - 11 speeds'), #GRX 11
        ('30-27-24-21-19-17-16-15-14-13-12-11',   '11T-30T - 12 speeds'), #GRX 12 #DuraAce 12 #Ultegra 12
        ('32-28-24-21-18-15-13-11',               '11T-32T - 8 speeds'), #Claris 8
        ('32-28-24-21-19-17-15-13-11',            '11T-32T - 9 speeds'), #Alivio 9 #Acera 9 #Altus 9
        ('32-28-25-22-20-18-16-14-12-11',         '11T-32T - 10 speeds'), #GRX 10 #Tiagra 10
        ('32-28-25-22-20-18-16-14-13-12-11',      '11T-32T - 11 speeds'), #GRX 11
        ('32-28-25-22-19-17-16-15-14-13-12-11',   '11T-32T - 12 speeds'), #Chorus 12 #Super Record 12 #Record 12
        ('34-28-24-21-18-15-13-11',               '11T-34T - 8 speeds'), #Claris 8
        ('34-30-26-23-20-17-15-13-11',            '11T-34T - 9 speeds'), #Alivio 9 #Acera 9 #Altus 9
        ('34-30-26-23-21-19-17-15-13-11',         '11T-34T - 10 speeds'), #GRX 10 #Tiagra 10
        ('34-30-27-25-23-21-19-17-15-13-11',      '11T-34T - 11 speeds'), #GRX 11
        ('34-30-27-24-21-19-17-15-14-13-12-11',   '11T-34T - 12 speeds_'), #GRX 12 #Shimano 105 12 #Dura Ace 12 #Ultegra 12
        ('34-29-25-22-19-17-16-15-14-13-12-11',   '11T-34T - 12 speeds'), #Chorus 12 #Super Record 12 #Record 12
        ('36-30-26-23-20-17-15-13-11',            '11T-36T - 9 speeds'), #Alivio 9 #Acera 9 #Altus 9
        ('36-32-28-24-21-19-17-15-13-11',         '11T-36T - 10 speeds'), #GRX 10 # Deore 10
        ('36-32-28-24-21-19-17-15-14-13-12-11',   '11T-36T - 12 speeds'), #GRX 12 #Shimano 12
        ('38-30-24-21-18-15-13-11',               '11T-38T - 8 speeds'), #Acolyte 8
        ('38-32-28-24-21-18-15-13-11',            '11T-38T - 9 speeds'), #Advent 9
        ('38-32-28-24-21-19-17-15-13-11',         '11T-38T - 10 speeds'), #Sword 10
        ('40-35-31-27-24-21-19-17-15-13-11',      '11T-40T - 11 speeds'), #GRX 11
        ('42-34-28-24-21-18-15-13-11',            '11T-42T - 9 speeds'), #Advent 9
        ('42-37-32-28-24-21-18-15-13-11',         '11T-42T - 10 speeds'), #Deore 10
        ('42-37-32-28-24-21-19-17-15-13-11',      '11T-42T - 11 speeds'), #GRX 11 #Deore 11
        ('42-36-32-28-24-21-19-17-15-13-11',      '11T-42T - 11 speeds_'), #All Road 11
        ('43-36-30-26-23-20-17-15-13-11',         '11T-43T - 10 speeds'), #Deore 10
        ('44-38-32-28-24-21-19-17-15-13-12-11',   '11T-44T - 12 speeds'), #Apex 12
        ('45-39-34-30-26-23-20-17-15-13-11',      '11T-45T - 11 speeds'), #Cues 11
        ('46-37-30-24-21-18-15-13-11',            '11T-46T - 9 speeds'), #Advent 9
        ('46-37-32-28-24-21-18-15-13-11',         '11T-46T - 10 speeds'), #Deore 10
        ('46-37-32-28-24-21-19-17-15-13-11',      '11T-46T - 11 speeds'), #GRX 11
        ('48-40-34-28-24-21-18-15-13-11',         '11T-48T - 10 speeds'), #Sword 10 #Advent X 10
        ('50-43-36-30-26-23-20-17-15-13-11',      '11T-50T - 11 speeds'), #Cues 11 #Deore XT 11
        ('50-42-36-32-28-25-22-19-17-15-13-11',  '11T-50T - 12 speeds'), #SX Eagle 12 #NX Eagle 12
        ('51-45-39-33-28-24-21-18-15-13-11',      '11T-51T - 11 speeds'), #Deore 11
        ('23-21-19-17-15-14-13-12',               '12T-23T - 8 speeds'), #Claris 8
        ('25-23-21-19-17-15-13-12',               '12T-25T - 8 speeds'), #Claris 8
        ('25-23-21-19-17-15-14-13-12',            '12T-25T - 9 speeds'), #Sora 9
        ('25-23-21-19-18-17-16-15-14-13-12',      '12T-25T - 11 speeds'), #GRX 11
        ('28-25-23-21-19-17-15-14-13-12',         '12T-28T - 10 speeds'), #GRX 10 #Tiagra 10
        ('42-34-28-24-21-18-15-12',               '12T-42T - 8 speeds'), #Acolyte 8
        ('46-37-30-24-21-18-15-12',               '12T-46T - 8 speeds'), #Acolyte 8
        ('25-23-21-19-17-16-15-14-13',            '13T-25T - 9 speeds'), #Sora 9
        ('26-23-21-19-17-15-14-13',               '13T-26T - 8 speeds'), #Claris 8
        ('25-23-21-19-18-17-16-15-14',            '14T-25T - 9 speeds'), #Sora 9
        ('28-25-23-21-20-19-18-17-16-15-14',      '14T-28T - 11 speeds') #GRX 11
    ]

    teeth_cassette = forms.ChoiceField(choices=teeth_cassette_choices, widget=forms.Select(attrs={'id':'id_teeth_cassette'}))