// Tipos de Datos en JavaScript
/*
La sintaxis en lo que es comentarioas 
es muy similar a la de Java
realmente diriamos que es identica 
*/
//Tipo String
var nombre = "Romina"; 
console.log(nombre);
nombre = 7;
console.log(typeof nombre);

//Tipo númerico
var numero = 3000;
console.log(numero);

//Tipo objeto
var objeto = {
    nombre:"Romina",
    apellido:"Rodriguez",
    telefono:"2618907766"
}
console.log(typeof objeto);

//Tipos de Datos Booleanos
var bandera = true;
console.log(typeof bandera);

//Tipo de dato de una Función
function miFuncion(){}
console.log(typeof miFuncion);

//Tipo de dato symbol
var simbolo = Symbol("mi simbolo");
console.log(typeof simbolo);

//Tipo de dato clase
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;  
    }
}
console.log(Persona);