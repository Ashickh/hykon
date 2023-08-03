$(document).ready(function () {
    $('input[name="address"]').change(function() {
        var selectedValue = $('input[name="address"]:checked').val();
        $('#selected_address').val(selectedValue);
    });

    $('#continue_checkout').click(function(){

        console.log("........!!!")
        var selectedAddressId = $('#selected_address').val(); // replace with the ID of the selected address
        var url = "/order/checkout-summary?address=" + selectedAddressId;
        console.log(url);
        window.location.href = url;
        console.log(window.location.href);
        
    });


    
//    href="{% url 'checkout-summary' %}"
});