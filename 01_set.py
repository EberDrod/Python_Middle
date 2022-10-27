#Definir conjuntos OJO verificar no son listas ni diccionarios

set_countries = {'col','mex', 'bol'}
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 2, 443, 23}
print(set_numbers)


set_types = {1, 'hola', False, 12.12}
print(set_types)

set_from_string = set('hoola')
print(set_from_string)

#Crear conjunto atraves de una tupla va con ((''))


set_from_tuples = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuples)


numbers = [1,2,3,1,3,4] #Esto esta definido como lista
set_numbers = set(numbers) #Se cambia para conjunto
print(set_numbers)
#El resultado convierte en Array 
unique_numbers = list(set_numbers)
print(unique_numbers)