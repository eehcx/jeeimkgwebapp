
function mostrarImagen(index) {
$('.work-img').hide();
$('.work-img').eq(index).show();
}

var index = 0;

mostrarImagen(index);

$('.prev').click(function() {
index--;
if (index < 0) {
    index = $('.work-img').length - 1;
}
mostrarImagen(index);
});

$('.next').click(function() {
index++;
if (index >= $('.work-img').length) {
    index = 0;
}
mostrarImagen(index);
});

function cambiarImagenAutomaticamente() {
    index++;
    if (index >= $('.work-img').length) {
        index = 0;
    }
    $('.work-img').eq(index - 1).fadeOut(900);
    $('.work-img').eq(index).fadeIn(900);
    mostrarImagen(index);
}

setInterval(cambiarImagenAutomaticamente, 5000);
