# -*- coding: utf-8 -*-

# Transformación de una formula en forma clausal
# Input: cadena de la formula en notacion inorder
# Output: lista de listas de literales

# Importando la libreria FNC
import FNC as fn
letrasProposicionalesA = ['p', 'q', 'r', 's', 't']
# # Formula a la cual encontrar su forma clausal
f1 = "((p>-q)>r)"
f2 = "-(-p>(rO-q))"
f3 = "(((pY-q)Y-r)O((-pYq)Y-r))"
# Aplicando el algoritmo de Tseitin a formula
# Se obtiene una cada que representa la formula en FNC
f1FNC = fn.Tseitin(f1, letrasProposicionalesA)
f2FNC = fn.Tseitin(f2, letrasProposicionalesA)
f3FNC = fn.Tseitin(f3, letrasProposicionalesA)

# Se obtiene la forma clausal como lista de listas de literales
f1Claus = fn.formaClausal(f1FNC)
f2Claus = fn.formaClausal(f2FNC)
f3Claus = fn.formaClausal(f3FNC)
# Imprime el resultado en consola
print("La formula clausal de f1 es")
print(f1Claus)

print("La formula clausal de f2 es")
print(f2Claus)

print("La formula clausal de f3 es")
print(f3Claus)
