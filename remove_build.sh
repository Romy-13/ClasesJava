#!/bin/bash

# Encuentra y elimina todos los directorios "build" en el repositorio
find . -type d -name "build" -exec git rm -r --cached {} \;

# Realiza un commit para guardar los cambios
git commit -m "Eliminar directorios de construcción en todos los proyectos"

# Realiza un push para actualizar el repositorio remoto
git push origin main
