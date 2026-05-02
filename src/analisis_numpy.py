import numpy as np

def cargar_datos(ruta_archivo):
    datos = np.genfromtxt(ruta_archivo, delimiter=',', dtype=str, skip_header=1, encoding='utf-8')
    return datos

def analizar_por_categoria(datos):
    categorias = datos[:, 5]
    totales = datos[:, 8].astype(float)
    categorias_unicas = np.unique(categorias)

    print("\n── Total de ventas por categoria ──")
    for cat in categorias_unicas:
        mascara = categorias == cat
        total_cat = np.sum(totales[mascara])
        promedio_cat = np.mean(totales[mascara])
        print(f"{cat}: total = ${total_cat:.2f} | promedio = ${promedio_cat:.2f}")

    totales_por_cat = np.array([np.sum(totales[categorias == c]) for c in categorias_unicas])
    print(f"\nCategoria con mayor venta: {categorias_unicas[np.argmax(totales_por_cat)]}")
    print(f"Categoria con menor venta: {categorias_unicas[np.argmin(totales_por_cat)]}")

def filtrar_categoria(datos, categoria):
    mascara = datos[:, 5] == categoria
    filtrado = datos[mascara]
    totales = filtrado[:, 8].astype(float)
    cantidades = filtrado[:, 6].astype(float)

    print(f"\n── Categoria filtrada: {categoria} ──")
    print(f"Registros encontrados: {len(filtrado)}")
    print(f"Suma total: ${np.sum(totales):.2f}")
    print(f"Promedio por venta: ${np.mean(totales):.2f}")
    print(f"Venta maxima: ${np.max(totales):.2f}")
    print(f"Venta minima: ${np.min(totales):.2f}")
    print(f"Total unidades: {np.sum(cantidades):.0f}")
    print(f"Diferencia venta maxima menos minima: ${np.max(totales) - np.min(totales):.2f}")
    print(f"Division promedio entre cantidad promedio: ${np.mean(totales) / np.mean(cantidades):.2f}")

if __name__ == "__main__":
    ruta = '../data/retail_sales_dataset.csv'
    datos = cargar_datos(ruta)

    print(f"Dataset cargado: {datos.shape[0]} filas, {datos.shape[1]} columnas")

    analizar_por_categoria(datos)
    filtrar_categoria(datos, 'Electronics')