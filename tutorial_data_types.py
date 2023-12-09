
#Datatypes

# city = 'Bangalore'
city = "Bangalore"
print(type(city))

age = 34
print(type(age))

marks = 98.75
print(type(marks))

is_programmer = True
print(type(is_programmer))

sample_variable = None
print(type(sample_variable))

#list
sample_list = [2,4,5.5,'Bangalore']
print(type(sample_list))
print(sample_list[0])
sample_list[1] = 0
print(sample_list)

#Set
sample_set = {2,3,0,5.5,'Bangalore'}
print(type(sample_set))
print(sample_set)
sample_set_duplicates = {2,2,0,5.5,'Bangalore'}
print(sample_set_duplicates)

#Tuples
sample_tuples = (2,3,1,5.25,'Bangalore')
print(type(sample_tuples))
print(sample_tuples[0])
#sample_tuples[0] = 0 NOT POSSIBLE
print(sample_tuples)

#Dict
sample_dict = {'name': 'john', 'age': '34'}
print(type(sample_dict))
print(sample_dict)
print(sample_dict.get('name'))
sample_dict_duplicates = {'name': 'john', 'name': 'john', 'age': '34'}
print(sample_dict)
