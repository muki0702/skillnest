let contador = 0;
let numero = document.getElementById("id-numero");
numero.textContent = "0 likes";

function sumar(){
    contador ++;
    document.getElementById("id-numero").innerText = (contador + " likes");
}

function restar(){
    contador --;
    document.getElementById("id-numero").innerText = (contador + " likes");
}