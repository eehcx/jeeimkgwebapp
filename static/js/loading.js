/*
document.addEventListener("DOMContentLoaded", function() {
    var lazyloadImages;

    if ("IntersectionObserver" in window) {
    lazyloadImages = document.querySelectorAll(".contact-header");
    var imageObserver = new IntersectionObserver(function(entries, observer) {
        entries.forEach(function(entry) {
        if (entry.isIntersecting) {
            var image = entry.target;
            image.style.backgroundImage = "url('" + image.getAttribute("data-src") + "')";
            observer.unobserve(image);
        }
        });
    });

    lazyloadImages.forEach(function(image) {
        imageObserver.observe(image);
    });
    }
});*/
document.addEventListener("DOMContentLoaded", function() {
    var lazyloadImages;

    if ("IntersectionObserver" in window) {
    lazyloadImages = document.querySelectorAll(".contact-header, .about-image, .work-img")
    var imageObserver = new IntersectionObserver(function(entries, observer) {
        entries.forEach(function(entry) {
        if (entry.isIntersecting) {
            var image = entry.target;
            image.style.backgroundImage = "url('" + image.getAttribute("data-src") + "')";
            observer.unobserve(image);
        }
        });
    });

    lazyloadImages.forEach(function(image) {
        setTimeout(function() {
        image.classList.remove("low-res");
        imageObserver.observe(image);
<<<<<<< HEAD
<<<<<<< HEAD
        }, 2000);
=======
        }, 1000);
>>>>>>> 51f44e72d358fc01d9edcdb3088647efb2468ed2
=======
        }, 1000);
>>>>>>> 51f44e72d358fc01d9edcdb3088647efb2468ed2
    });
    }
});