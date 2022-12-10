#Esta función e para traer todos os countries que están nos .txt
#Teño que crear unha tupla porque é o que lle hai que pasar o dropdown
#country_list=[]
with open("terrameiga/static/lists/country_list_en.txt", "r") as country_list_file:
    #for country in country_list_file:
     #   country_list.append(country)
    #print(country_list)

    country_list = [tuple([x,x]) for x in country_list_file]

    print(country_list)



# from django import forms

# INTEGER_CHOICES= [tuple([x,x]) for x in range(1,32)]

# print(INTEGER_CHOICES)

