const waitElement = $('#update_header');
waitElement.on('click', () => {
    $('header').text('New Header!!!');
});
