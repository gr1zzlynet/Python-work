names = ['Ragnar', 'Tynn', 'Vlad', 'Ildar']
message = f"Hello {names[0]}!"
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[1] = 'ducati'
print(motorcycles)

motorcycles.append('moto')
print(motorcycles)

motocicletas = []
motocicletas.append('bici')
motocicletas.append('bike')
motocicletas.append('baik')
print(motocicletas)

motorcycles.insert(2, 'harley')
print(motorcycles)

del motorcycles[2]
print(motorcycles)

popped_motocycle = motorcycles.pop()
print(motorcycles)
print(popped_motocycle)


motorcycles.remove('honda')
print(motorcycles)

comida = ['leche', 'carne', 'frijoles', 'azucar']
muy_caro = 'azucar'
comida.remove(muy_caro)
print(comida)
print(f"\nEl {muy_caro.title()} is too expensive for me.")