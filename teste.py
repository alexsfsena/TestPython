# -*- coding: latin1 -*-
#**** Uma lista de instrumentos musicais
#instrumentos = ['Baixo', 'Bateria', 'Guitarra']
# Para cada nome na lista de instrumentos
#for instrumento in instrumentos:
 #mostre o nome do instrumento musical
# print instrumento
#temp = int(raw_input('Entre com a temperatura: '))
#if temp < 0:
#	print 'Congelando...'
#elif 0 <= temp <= 20:
#	print 'Frio'
#elif 21 <= temp <= 25:
#	print 'Normal'
#elif 26 <= temp <= 35:
#	print 'Quente'
#else:
#	print 'Muito quente!'

#contador
#cont = 0
#for x in range(1, 20):
#	print x	
#	cont = cont+x
#	print ("cont:", cont)
#print cont


# Convertendo de real para inteiro
#print 'int(3.14) =', int(3.14)
# Convertendo de inteiro para real
#print 'float(5) =', float(5)
# Calculo entre inteiro e real resulta em real
#print '5.0 / 2 + 3 = ', 5.0 / 2 + 3
# Inteiros em outra base
#print "int('20', 8) =", int('20', 8) # base 8
#print "int('20', 16) =", int('20', 16) # base 16

# Operacoes com números complexos
#c = 3 + 4j
#print 'c =', c
#print 'Parte real:', c.real
#print 'Parte imaginária:', c.imag
#print 'Conjugado:', c.conjugate()
s = 'Camel'
# Concatenação
print 'The ' + s + ' run away!'
# Interpolação
print 'tamanho de %s => %d' % (s, len(s))
# String tratada como sequência
for ch in s: print ch
# Strings são objetos
if s.startswith('C'): print s.upper()
# o que acontecerá?
print 3 * s
# 3 * s é consistente com s + s + s

print 'isto e um teste'[::-1]
