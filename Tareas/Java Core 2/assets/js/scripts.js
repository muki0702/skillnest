let likes = [0,0,0]
let spans =[
    document.querySelector("#publicacion-1"),
    document.querySelector("#publicacion-2"),
    document.querySelector("#publicacion-3")
]
function like(id) {
    likes[id] ++;
    spans[id].innerText = likes[id]
}