# -*- coding: latin1 -*-

def ParaCelsius(far):
	celsius = (far - 32)/1.8
	return celsius
	
def ParaFarenheigt(celsius):
	farenheit = (celsius * 1.8)+32
	return farenheit
print ('74 F sao',ParaCelsius(74),'C')
print ('74 C sao', ParaFarenheigt(74),'F')
