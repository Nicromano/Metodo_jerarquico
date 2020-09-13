# Metodo_jerarquico

Para empezar las importaciones de las librerias deben ser las siguientes 

```
from Jerarquico import agruparCluster
from Distancias import calculaDistancia
```

Es posible obtener la matriz de distancias llamando a la función:

```
calculaDistancia(datos, metodo)
```

Tal que: 
- Datos, es un dataframe de Pandas con los datos correspondiente
- metodo, es el metodo a usar, puede ser: "euclidean" "manhattan" "pearson"
retorna un Dataframe con las distancias obtenidas

Luego de este se procede a realizar el enlace correspondiente con la función:
```
agruparCluster(matriz, enlace, metodo)
```

Tal que:
- Matriz, es un dataFrame que corresponde a la matriz de distancia de los datos 
- enlace, es el tipo de enlace a usar: "simple", "completo", "promedio"
- metodo, es un parámetro opcional que especifica el metodo usado en la matriz de distancia

Retorna:
- La matriz resultante
- las distancia 
- Los cluster agrupados

