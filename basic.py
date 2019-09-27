/*Los tipos de datos string o cadenas de caractéres son ampliamente usados en la administración y
análisis de datos. Python soporta el uso de dos diversos tipo de cadenas: ASCII y Unicode.*/
/*
Las cadenas ASCII se delimitan por ’...’, "..." o """...""". Las comillas triples delimitan cadenas
multilínea. 
Las cadenas Unicode comienzan con un u seguido por la cadena conteniendo
caracteres Unicode.
• Unicode es un estándar de codificación de caracteres diseñado para facilitar el tratamiento
de textos de múltiples lenguajes. Una cadena Unicode puede convertirse en una cadena
ASCII seleccionando una codificación, por ejemplo el utf-8.*/

a = 'Aprender Python es fácil'
b = u'Aprender Python es fácil'
c = b.encode('utf-8')
d = b.encode('utf-16')
e = b.encode('latin-1')

print('La versión de Python es ' + str(3) + '.' + str(6))
print('La versión de Python es %s.%s' % (3, 6))
print('La versión de Python es %.1f' % (3.6))
print('La versión de Python es %.3f' % (3.611232138167))
print('La versión de Python es %(numero)s.%(decimal)s' % dict(numero=3, decimal=6))
print('La versión de Python es {0}.{1}'.format(3, 6))
print('La versión de Python es {0:.1f}'.format(3.611232138167))
print('La versión de Python es {numero}.{decimal}'.format(numero=3, decimal=6))
print('La versión de Python es {numero:.1f}'.format(numero=3.611232138167))
