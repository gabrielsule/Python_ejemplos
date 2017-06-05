choices = dict(
    one = 'primero'
    ,dos = 'segundo'
    ,tres = 'tercero'
    ,cuatro = 'cuarto'
)
v = 'nueve'

# print(choices[v])
print(choices.get(v, 'otro numero'))    #fix si no existe el numero