from django.contrib import admin
from django.urls import path, include  # importar include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_hola.urls')),  # incluir las URLs de la app
    path('', include('app_info.urls')),
    path('', include('app_estudiante.urls')),  # incluir las URLs de la app
    path('', include('app_saludo.urls')),  # incluir las URLs de la app
    path('', include('app_libro.urls')),  # incluir las URLs de la app
    path('', include('app_ejemplo01.urls')),  # incluir las URLs de la app
    path('', include('app_ejemplo02.urls')),  # incluir las URLs de la app
]
libro_list.html
<!-- app_ejemplo02/templates/app_ejemplo02/libro_list.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Lista de Libros</title>
</head>
<body>
    <h1>Lista de Libros</h1>

    <a href="{% url 'libro_create' %}">Agregar nuevo libro</a>
    <ul>
        {% for libro in libros %}
            <li>
                <a href="{% url 'libro_detail' libro.pk %}">{{ libro.titulo }}</a> - {{ libro.autor }}
                (<a href="{% url 'libro_update' libro.pk %}">Editar</a> |
                <a href="{% url 'libro_delete' libro.pk %}">Eliminar</a>)
            </li>
        {% empty %}
            <li>No hay libros disponibles.</li>
        {% endfor %}
    </ul>
</body>
</html>
libro_detail.html
<!-- app_ejemplo02/templates/app_ejemplo02/libro_detail.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Detalle del Libro</title>
</head>
<body>
    <h1>{{ libro.titulo }}</h1>
    <p><strong>Autor:</strong> {{ libro.autor }}</p>

    <p>
        <a href="{% url 'libro_update' libro.pk %}">Editar</a> |
        <a href="{% url 'libro_delete' libro.pk %}">Eliminar</a> |
        <a href="{% url 'libro_list' %}">Volver a la lista</a>
    </p>
</body>
</html>
libro_form.html
<!-- app_ejemplo02/templates/app_ejemplo02/libro_form.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Formulario de Libro</title>
</head>
<body>
    <h1>{{ view.object.pk|yesno:"Editar Libro,Nuevo Libro" }}</h1>

    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Guardar</button>
    </form>

    <a href="{% url 'libro_list' %}">Cancelar</a>
</body>
</html>
________________________________________
libro_confirm_delete.html
<!-- app_ejemplo02/templates/app_ejemplo02/libro_confirm_delete.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Confirmar eliminación</title>
</head>
<body>
    <h1>Eliminar libro</h1>
    <p>¿Estás seguro que deseas eliminar <strong>{{ object.titulo }}</strong>?</p>

    <form method="post">
        {% csrf_token %}
        <button type="submit">Sí, eliminar</button>
    </form>

    <a href="{% url 'libro_list' %}">Cancelar</a>
</body>
</html>
