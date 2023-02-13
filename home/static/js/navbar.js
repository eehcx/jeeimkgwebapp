//Ocultar barra de navegación cuando se haga scroll down

let ubicacionPrincipal = window.pageYOffset;
window.onscroll = function () {
    let Desplazamiento_Actual = window.pageYOffset;
    if (ubicacionPrincipal >= Desplazamiento_Actual) {
        document.getElementById('navbar').style.top = '0';
    }
    else {
        document.getElementById('navbar').style.top = '-110px';
    window.addEventListener("scroll", function () {
        var nav = document.querySelector("nav");
        nav.classList.toggle("down", window.scrollY > 100);
    })
    }
    ubicacionPrincipal = Desplazamiento_Actual;
}
