$(document).ready(function () {
    $('#add_to_cart').click(function(){
        $.ajax({
            url: "/order/add-cart/",
            type : "POST",
            data: {
                'product_slug': $(this).data('product_slug'),
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                window.location.href = '/order/carts/';
            }
        });       
    });
      
});

// function applyFilters(event) {
//     event.preventDefault(); // prevent default form submission
//     const formData = new FormData(event.target); // get form data
//     const filters = Object.fromEntries(formData.entries()); // convert to object
//     const url = '/filter'; // URL to your Django view
//     const xhr = new XMLHttpRequest(); // create AJAX request object
//     xhr.open('POST', url); // set request method and URL
//     xhr.setRequestHeader('Content-Type', 'application/json'); // set request header
//     xhr.onload = function() {
//       // handle response from server
//       const response = JSON.parse(xhr.responseText);
//       // update content on page
//     }
//     xhr.send(JSON.stringify(filters)); // send request with selected filters as JSON
//   }
  
//   document.getElementById('filter-form').addEventListener('submit', applyFilters);


