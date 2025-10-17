const sesion = document.getElementById("inicio")
const seccion = document.getElementById("cambiar")
let reemplazo = ["Ficción", "Históricos", "Tecnología", "Autoayuda", "Poesía"]
function clickeo(id){
    seccion.innerHTML = reemplazo[id]
}
sesion.addEventListener("click", () =>{
    alert("Inicio de Sesión exitoso")
})
let libros_lista = [
    document.getElementById("boton1"),
    document.getElementById("boton2"),
    document.getElementById("boton3")
]
function cambiar(id){
    libros_lista[id].style.backgroundColor = "Maroon";
    libros_lista[id].textContent = "No Disponible";
    libros_lista[id].style.color = "aliceblue"
}