# Einstein

El módulo `Einstein` proporciona una colección de fórmulas desarrolladas por Albert Einstein, organizadas en diferentes clases según sus teorías más importantes, como la Relatividad Especial, la Relatividad General y el Efecto Fotoeléctrico.

## Instalación

Para utilizar este módulo, sigue los siguientes pasos:

1. Clona el repositorio desde GitHub:

```bash
git clone https://github.com/tu_usuario/einstein.git
```

2. Navega al directorio del proyecto:

```bash
cd einstein
```

3. Asegúrate de tener Python instalado en tu sistema. Puedes verificar la instalación de Python ejecutando:

```bash
python --version
```

## Uso

A continuación, se presentan ejemplos de uso para las diferentes clases y métodos disponibles en el módulo.

### Importación del módulo

```python
import einstein
```

## Relatividad Especial

### Energía según E=mc²

```python
masa = 1.0  # kg
energia = einstein.RelatividadEspecial.energia_mc2(masa)
print(f"Energía (E=mc^2): {energia} J")
```

### Dilatación del tiempo

```python
t = 1.0  # s
v = 100000  # m/s
tiempo_dilatado = einstein.RelatividadEspecial.dilatacion_tiempo(t, v)
print(f"Tiempo dilatado: {tiempo_dilatado} s")
```

### Contracción de la longitud

```python
L = 1.0  # m
v = 100000  # m/s
longitud_contraida = einstein.RelatividadEspecial.contraccion_longitud(L, v)
print(f"Longitud contraída: {longitud_contraida} m")
```

### Energía relativista total

```python
masa = 1.0  # kg
p = 1.0  # kg*m/s
energia_total = einstein.RelatividadEspecial.energia_relativista_total(masa, p)
print(f"Energía relativista total: {energia_total} J")
```

### Energía cinética relativista

```python
masa = 1.0  # kg
v = 100000  # m/s
energia_cinetica = einstein.RelatividadEspecial.energia_cinetica_relativista(masa, v)
print(f"Energía cinética relativista: {energia_cinetica} J")
```

## Relatividad General

### Ecuación de Friedmann

```python
rho = 1e-26 # kg/m^3
k = 0
a = 1.0
Lambda = 0.0
tasa_expansion = einstein.RelatividadGeneral.ecuacion_friedmann(rho, k, a, Lambda)
print(f"Tasa de expansión del universo (Friedmann): {tasa_expansion} s^-1")
```

## Efecto Fotoeléctrico

### Energía del efecto fotoeléctrico

```python
frecuencia = 5e14 # Hz
funcion_trabajo = 2.28e-19 # J
energia_fotoelectrica = einstein.EfectoFotoelectrico.energia_fotoelectrico(frecuencia, funcion_trabajo)
print(f"Energía del efecto fotoeléctrico: {energia_fotoelectrica} J")
```

## Configuración

...

## Contribución

...

## Créditos

...

## Licencia

Sistema Skanilo se distribuye bajo la Licencia Pública General de GNU (GPL). Consulta el archivo LICENSE para obtener más detalles.

## Contacto

Author: Johannes Rosenkranz Cordovez Email: jfronz@gmail.com

## Notas Adicionales

...
