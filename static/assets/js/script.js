var swiper = new Swiper('.events-cards', {
    spaceBetween: 30,
    effect: 'fade',
    loop: true,
    // autoHeight: true,
    pagination: {
        el: '.events-cards__pagination',
        clickable: true,
    }
});