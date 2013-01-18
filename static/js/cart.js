$(document).ready(function() {
    $('.del-cart-item').on('click', function(e) {
        e.preventDefault();
        var self = $(this);
        var data = $(this).data();
        $.get(data.url, function(data) {
            if (data.result === true) {
                    self.parent().parent().remove();
                    $('.total').text(data.subtotal + ' руб.');
                    $('.subtotal-cart-box').text(data.subtotal);
                    $('.cart-box-count').text(data.count_box);
                    if (!$('.cartitem').length) {
                        window.location.reload()
                    }
            }
        });
    })
});