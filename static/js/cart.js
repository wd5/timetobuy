$(document).ready(function() {
    $('.del-cart-item').on('click', function() {
        var self = $(this);
        var data = $(this).data();
        $.get(data.url, function(data) {
            if (data.result === true) {
                self.parent().parent().remove();
                $('.total').text(data.subtotal + ' руб.')
            }
        });
    })
});