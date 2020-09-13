# Metodo jerárquico

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
- Enlace, es el tipo de enlace a usar: "simple", "completo", "promedio"
- Método, es un parámetro opcional que especifica el método usado en la matriz de distancia

Retorna:
- La matriz resultante
- Las distancia entre cada cluster
- Los cluster agrupados

## Ejemplo 1 

Método jerárquico con matriz de distancia obtenida previamente 
```
data = pd.read_csv('data.csv', sep=',', header=None)
matriz_distancia = calculaDistancia(data, 'euclidean')
matriz_result, cluster, agrupaciones = agruparCluster(matriz_distancia, 'promedio')

``` 

## Ejemplo 2

Método jerárquico con dato inicial, datos en crudo sin matriz de distancia 

```
data = pd.read_csv('Dataset.csv', sep=',', header=None)
matriz_result, cluster, agrupaciones = agruparCluster(data, 'promedio', 'eucliean')

``` 
