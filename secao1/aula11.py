a = "A"
b = 'B'
c = 3.1415

string = 'a={} b={} c={}'
formato = string.format(a, b, c)

string1 = 'a={0} b={1} c={2}'
formato1 = string1.format(a, b, c)

string2 = 'b={1} a={0} c={2}'
formato2 = string2.format(a, b, c)

string3 = 'b={nome2} a={nome1} c={nome3}'
formato3 = string3.format(nome1=a, nome2=b, nome3=c)
''' caso um argumento seja nomeado, todos os que estão depois 
deste tbm devem ser nomeados'''

print(formato, formato1, formato2, formato3, sep='\n')