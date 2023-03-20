# agappTemplate
Este es un simple template de una aplicación web en Python Flask para propósitos de prueba y demostración. La imagen de Docker puede ser fácilmente desplegada en cualquier servidor que soporte Docker, convirtiéndolo en una elección ideal para una variedad de escenarios de aplicación web. El código fuente y el Dockerfile están disponibles en GitHub, lo que permite una fácil personalización y extensión de la aplicación. 

Aqui encontraras un archivo Dockerfile y otros archivos relacionados a una aplicación Flask que se encontraba en ejecución dentro de un contenedor. Incluye los manifiestos de deployment, service, y ingress.

Además, se han agregado los probes de Kubernetes necesarios para validar que el servicio esté funcionando correctamente. Sigue los pasos descritos en este documento para asegurarte de que la aplicación Flask esté ejecutándose sin problemas.

Todos los archivos respestivos los encontraras en la carperta de Improved:
https://github.com/LeoSanz/agappTemplate/tree/main/Improved

Para una vista rapida ejecuta:
```console
docker run -d -p 5000:5000 leosanz/agapp:latest
```
