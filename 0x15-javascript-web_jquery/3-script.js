const waitElement = $('#red_header');
waitElement.on('click', () => {
    $('header').addClass('red');
});
