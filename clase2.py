import numpy as np

riesgo_personal = 0.05
riesgo_empresarial = 0.1
print("Riesgo del crédito personal:", riesgo_personal)
print("Riesgo del crédito empresarial:", riesgo_empresarial)

# Matriz de coeficientes
A = np.array([
    [1, 1],
    [riesgo_personal, riesgo_empresarial]
])
print("Matriz de coeficientes A:")
print(A)

# Restricciones
b = np.array([100, 7])
print("\nVector de restricciones b:")
print(b)

# Resolver sistema
sol = np.linalg.solve(A, b)

print("Solución del sistema:")
print(sol)


# Interpretación de la solución
x, y = sol
print("Crédito personal:", x)
print("Crédito empresarial:", y)

# Validación de la solución
print("\nValidación de la solución:")
print("Capital:", x + y)
print("Riesgo:", riesgo_personal * x + riesgo_empresarial * y)


# Transformación Lineal: Convertir créditos en métricas

retorno_esperado_personal = 0.12
retorno_esperado_empresarial = 0.15

T = np.array([
    [riesgo_personal, retorno_esperado_personal],  
    [riesgo_empresarial, retorno_esperado_empresarial]    
])

print("\nMatriz de transformación T:")
print(T)

decision = np.array([x, y])
print("\nVector de decisión (créditos):")
print(decision)

resultado = np.dot(T, decision)

print("\nResultado de la transformación lineal:")
print(resultado)

riesgo, retorno = resultado
print("Riesgo:", riesgo)
print("Retorno:", retorno)

# Sistema inconsistente
A_bad = np.array([
    [1, 1],
    [1, 1]
])
print("\nMatriz de coeficientes A_bad:")
print(A_bad)

b_bad = np.array([100, 120])
print("\nVector de restricciones b_bad:")
print(b_bad)

try:
    np.linalg.solve(A_bad, b_bad)
except np.linalg.LinAlgError as e:
    print("\nError al resolver el sistema inconsistente:")
    print(e)

# Sistema con múltiples soluciones
# Sistema con infinitas soluciones

A_inf = np.array([
    [1, 1],
    [2, 2]
])
print("\nMatriz de coeficientes A_inf:")
print(A_inf)

b_inf = np.array([100, 200])
print("\nVector de restricciones b_inf:")
print(b_inf)

try:
    sol_inf = np.linalg.solve(A_inf, b_inf)
    print("\nSolución del sistema con infinitas soluciones:")
    print(sol_inf)
except np.linalg.LinAlgError as e:
    print("\nError al resolver el sistema con infinitas soluciones:")
    print(e)