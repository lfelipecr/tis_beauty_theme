$('#category_item_list').owlCarousel({
    smartSpeed: 1000,
    autoplay: true,
    autoplayHoverPause: true,
    nav: true,
    navText: [
        '<img src="images/prev.png" />',
        '<img src="images/next.png" />'
    ],
    dots: false,
    loop: true,
    margin: 10,
    responsive: {
        0: {
            items: 1
        },
        576: {
            items: 2
        },
        768: {
            items: 3
        },
        1000: {
            items: 4
        },
        1500: {
            items: 6
        }
    }
});


$('#products_item_list').owlCarousel({
    smartSpeed: 1000,
    autoplay: true,
    autoplayHoverPause: true,
    nav: true,
    navText: [
        '<img src="images/prev.png" />',
        '<img src="images/next.png" />'
    ],
    dots: false,
    loop: true,
    margin: 10,
    responsive: {
        0: {
            items: 1
        },
        576: {
            items: 1
        },
        768: {
            items: 2
        },
        1000: {
            items: 2
        },
        1500: {
            items: 3
        }
    }
});