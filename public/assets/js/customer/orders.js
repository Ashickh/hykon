var product_id = '';
var rating = '';
function popupRate(id){
    product_id = id;
    document.getElementById("rating").style.display="block";
    return false;
}
function closeModal(){
    document.getElementById("rating").style.display="none";
}

//star rating
const starRating = document.getElementsByName('rating');
starRating.forEach((input) => {
    input.addEventListener('change', () => {
        rating = input.value;
    });
});

$(document).ready(function () {
    $('#rate_product').click(function(){
        console.log(rating)
        if (rating == ''){
            $('#rating_error').text('Please give rating');
            $('#rating_error_div').show();
            setTimeout(function(){
               $('#rating_error_div').hide();
            }, 3000);
        }else if (!$('#title').val()){
            $('#rating_error').text('Please enter title');
            $('#rating_error_div').show();
            setTimeout(function(){
               $('#rating_error_div').hide();
            }, 3000);
        }else if (!$('#review').val()){
            $('#rating_error').text('Please enter review');
            $('#rating_error_div').show();
            setTimeout(function(){
               $('#rating_error_div').hide();
            }, 3000);
        }else{
            $.ajax({
                url: "/order/review-product/",
                type : "POST",
                data: {
                    'product_id': product_id,
                    'title': $('#title').val(),
                    'review': $('#review').val(),
                    'rating': rating,
                    'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
                },
                success: function (data) {
                    $('#rating_error').text('Review Saved Successfully');
                    $('#rating_error_div').show();
                    setTimeout(function(){
                       $('#rating_error_div').hide();
                       $('#title').val('');
                       $('#review').val('');
                       $('input[type=radio][name=rating]').prop('checked', false);
                       closeModal();
                    }, 1000);
                }
            });
        }
    });
});