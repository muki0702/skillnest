let edad = 27;
const nombre = "muki";
let calificaciones = [45,65,47,53];
let frutas_favoritas = ['papaya' ,'mango', 'melocoton'];
console.log(edad);
console.log(nombre);
console.log(calificaciones);
console.log(frutas_favoritas);

frutas_favoritas.push("guanabana")
console.log(frutas_favoritas)

for(fruta of frutas_favoritas) {
    console.log(fruta)
}
for(let i = 0; i< frutas_favoritas.length; i++){
    console.log(frutas_favoritas[i])
}
let contador = 0;
let evento = true;
while(evento === true){
    contador++;
    console.log(contador)
    if (contador === 10){
        evento = false
    }
}

function saludar(nombre){
    console.log("hola" + nombre)
}
nombre = "Pedro"

saludar(nombre)