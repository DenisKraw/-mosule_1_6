my_dict={'Denis':1987,'Anton':1988,'Kris':2000}
print(my_dict)
print(my_dict['Denis'])
my_dict['Natali']=1999
print(my_dict['Natali'])
my_dict.update({'Nikolaj':1977,
                'Anna':1998})
my_dict.pop('Anton')
print(my_dict)
my_set={1,2,2,3,True,'Katia','Katia'}
my_set.update({6,'Nikolaj'})
my_set.discard(2)
print(my_set)