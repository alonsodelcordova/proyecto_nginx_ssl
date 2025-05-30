FROM php:8.2-apache

# Instala mysqli y extensiones comunes
RUN docker-php-ext-install mysqli pdo pdo_mysql

copy . /var/www/html

# Habilita el módulo de reescritura de Apache (si lo necesitas)
RUN a2enmod rewrite