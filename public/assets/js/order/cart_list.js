$(document).ready(function () {
    $('.add_to_cart').click(function(){
        $.ajax({
            url: "/order/add-cart/",
            type : "POST",
            data: {
                'product_slug': $(this).data('product_slug'),
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                $('#add_remove_message_div').show();
                $("#add_remove_message").text('Product added to your cart')
                setTimeout(function() {
                    window.location.reload();
                }, 1000);
            }
        });
    });
    $('.remove_from_cart').click(function(){
        $.ajax({
            url: "/order/remove-cart/",
            type : "POST",
            data: {
                'product_slug': $(this).data('product_slug'),
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                $('#add_remove_message_div').show();
                $("#add_remove_message").text('Product removed from your cart')
                setTimeout(function() {
                    window.location.reload();
                }, 1000);
            }
        });
    });
    $('.delete_from_cart').click(function(){
        $.ajax({
            url: "/order/remove-cart/",
            type : "POST",
            data: {
                'delete': true,
                'product_slug': $(this).data('product_slug'),
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                setTimeout(function() {
                    window.location.reload();
                }, 1000);
            }
        });
    });
});