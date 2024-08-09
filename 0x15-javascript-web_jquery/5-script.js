const appendElement = $('#add_item')
appendElement.on('click', () => {
    $('UL.my_list').append('<li>Item</li>')
});
