const texto = document.getElementById("sesion")
const gato = document.getElementById("botonGato")
const perro = document.getElementById("botonPerro")
const definicion = document.getElementById("definicion")
let likes = [0,0]
let spans = [
    document.querySelector("#gato"),
    document.querySelector("#perro")
]
texto.addEventListener('click', () => {
    texto.innerText = "cerrar sesion";
});
    
gato.addEventListener('click', ()=> {
    alert('Gato Atigrado was liked');
});
perro.addEventListener('click', ()=> {
    alert('Golden Retriever was liked');
})
function like(id){
    likes[id] ++;
    spans[id].innerText = likes[id]
}
definicion.addEventListener('click', () =>{
    definicion.style.visibility = 'hidden'
})