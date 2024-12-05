from django.shortcuts import render
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64

def home(request):
    # Datos ficticios para las graficas
    line_data = {
        "labels": ["Enero", "Febrero", "Marzo", "Abril", "Mayo"],
        "values": [10, 20, 15, 30, 25]
    }

    bar_data = {
        "labels": ["A", "B", "C", "D"],
        "values": [5, 10, 15, 20]
    }

    scatter_x = np.random.rand(10).tolist()
    scatter_y = np.random.rand(10).tolist()

    pie_data = {
        "labels": ["Manzanas", "Naranjas", "Bananas"],
        "values": [30, 50, 20]
    }

    histogram_data = np.random.randn(100).tolist()

    box_data = {
        "values": [np.random.normal(0, std, 100).tolist() for std in range(1, 4)]
    }

    # Grafica de lineas
    fig, ax = plt.subplots()
    ax.plot(line_data["labels"], line_data["values"], marker='o')
    ax.set_title('Grafica de lineas')
    ax.set_xlabel('Meses')
    ax.set_ylabel('Valores')
    buffer = BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)
    line_chart = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    # Grafica de barras
    fig, ax = plt.subplots()
    ax.bar(bar_data["labels"], bar_data["values"])
    ax.set_title('Grafica de barras')
    ax.set_xlabel('Categorias')
    ax.set_ylabel('Valores')
    buffer = BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)
    bar_chart = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    # Grafica de dispersion
    fig, ax = plt.subplots()
    ax.scatter(scatter_x, scatter_y, color='r')
    ax.set_title('Grafica de dispersion')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    buffer = BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)
    scatter_chart = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    # Grafica de pastel
    fig, ax = plt.subplots()
    ax.pie(pie_data["values"], labels=pie_data["labels"], autopct='%1.1f%%', startangle=90)
    ax.set_title('Grafica de pastel')
    buffer = BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)
    pie_chart = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    # Grafica de histograma
    fig, ax = plt.subplots()
    ax.hist(histogram_data, bins=20, color='blue', edgecolor='black')
    ax.set_title('Grafica de histograma')
    ax.set_xlabel('Valor')
    ax.set_ylabel('Frecuencia')
    buffer = BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)
    histogram_chart = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    # Grafica de cajas
    fig, ax = plt.subplots()
    ax.boxplot(box_data["values"])
    ax.set_title('Grafica de cajas')
    buffer = BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)
    boxplot_chart = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    # Contexto para la plantilla
    context = {
        "line_chart": line_chart,
        "bar_chart": bar_chart,
        "scatter_chart": scatter_chart,
        "pie_chart": pie_chart,
        "histogram_chart": histogram_chart,
        "boxplot_chart": boxplot_chart,
    }

    return render(request, 'graficas/home.html', context)