nums = ['Uno','Dos','Tres','Cuatro','Cinco','Seis','Siete','Ocho','Nueve','Diez']
colors = ['Rojo','Azul','Verde','Amarillo','Naranja','Morado','Negro','Blanco','Gris','Rosa']

#print(nums)


#colors.append('Rojo')
#colors.extend(['Rojo','Azul'])

#colors.insert(0,'Violeta')
#colors.clear()
#colors.append('Violeta')
#print(colors)
#print(colors.pop(0))
#colors.sort(reverse=False)

#colors_1 =colors.copy()
#print(colors_1)
#print(colors)



"""for num in nums:
    
    output=f"Number: {num} color: {colors[nums.index(num)]}"   
    print(output)
"""

#print([nums[0],colors[0]])



nums.reverse()
Lista_nueva =[]
for num in nums:
    output=f" {num}    {colors[nums.index(num)]}"  
    Lista_nueva.append(output)
    
 
    
print (Lista_nueva)