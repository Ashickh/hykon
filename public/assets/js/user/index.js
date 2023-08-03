$(document).ready(function () {
    $('#register').click(function(e){
        event.preventDefault();
        if ($('#phone_email').val() == '' || $('#first_name').val() == '' || $('#password').val() == ''){
            if ($('#phone_email').val() == '')
                $('#register_error').text('Enter Email id');
            if ($('#first_name').val() == '')
                $('#register_error').text('Enter First Name');
            if ($('#password').val() == '')
                $('#register_error').text('Enter Password');
            $('#register_error_div').show();
            setTimeout(function(){
               $('#register_error_div').hide();
            }, 3000);
            return false;
        }
        else{
            $.ajax({
                url: "/user/register/",
                type : "POST",
                data: {
                    'email': $('#phone_email').val(),
                    'first_name': $('#first_name').val(),
                    'last_name': $('#last_name').val(),
                    'password': $('#password').val(),
                },
                success: function (data) {

                }
            });
        }
    });

    $('#log_btn').click(function(e){
        event.preventDefault();
        $('#login_div').show();
        $('#regitration_div').hide();
    });

    $('#show_register').click(function(e){
        event.preventDefault();
        $('#login_div').hide();
        $('#regitration_div').show();
    });

    $('#submit_login').click(function(e){
        event.preventDefault();
        if ($('#username').val() == '' || $('#login_password').val() == ''){
            if ($('#username').val() == '')
                $('#login_error').text('Enter Email');
            if ($('#login_password').val() == '')
                $('#login_error').text('Enter Password');
            $('#login_error_div').show();
            setTimeout(function(){
               $('#login_error_div').hide();
            }, 3000);
            return false;
        }
        else{
           
            $.ajax({
                url: "/user/login/",
                type : "POST",
                data: {
                    'username': $('#username').val(),
                    'password': $('#login_password').val(),
                },
                success: function (data) {
                    console.log(data);
                    if (data.status == 'success')
                        window.location.href = '/user/dashboard/'
                      
                    else{
                        $('#login_error').text(data.message);
                        $('#login_error_div').show();
                        setTimeout(function(){
                           $('#login_error_div').hide();
                        }, 3000);
                    }
                }
            });
        }
    });

    // for enquiry
    $('#enquiry').click(function(e){
       
        event.preventDefault();
        if ($('#name').val() == '' || $('#email').val() == '' || $('#place').val() == '' 
            ||$('#state').val() == '' ||$('#district').val() == '' ||$('#phone').val() == '' 
            ||$('#requirement').val() == '' ||$('#message').val() == '' ){
           
            if ($('#name').val() == '')
                $('#enquiry_error').text('Enter Name');
            if ($('#email').val() == '')
                $('#enquiry_error').text('Enter Email ID');
            if ($('#place').val() == '')
                $('#enquiry_error').text('Enter place');
            if ($('#state').val() == '')
                $('#enquiry_error').text('Enter state');
            if ($('#district').val() == '')
                $('#enquiry_error').text('Enter district');
            if ($('#phone').val() == '')
                $('#enquiry_error').text('Enter phone');
            if ($('#requirement').val() == '')
                $('#enquiry_error').text('Choose requirement');
            if ($('#message').val() == '')
                $('#enquiry_error').text('Enter message');
            $('#enquiry_error_div').show();
            setTimeout(function(){
                $('#enquiry_error_div').hide();
            }, 6000);
            return false;
        }

        else{
            
            var email = document.getElementById("email").value;
            // var phoneNumber = document.getElementById("phoneInput").value;
            var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            // var phonePattern = /^\d{10}$/;
            if (emailPattern.test(email)) {
        
                alert("Thanks for enquiring Hykon, Just wait for a while after clicking OK button. You will get an email shortly.!");

              } else {
              
                alert("Invalid email address!");
              }
            
            $.ajax({
                
                url: "enquiry/",
                type : "POST",
                data: {
                    'name': $('#name').val(),
                    'email': $('#email').val(),
                    'place': $('#place').val(),
                    'state': $('#state').val(),
                    'district': $('#district').val(),
                    'phone': $('#phone').val(),
                    'requirement': $('#requirement').val(),
                    'message': $('#message').val(),
                },
                success: function (data) {
                    console.log(data);
                    if (data.status == 'success')
                        window.location.href = ""

                    
                    }

                
            });
        }
    });

    $('#search').click(function(e){
        event.preventDefault();

        var myQueryParam = $('#key_word').val();
        console.log(myQueryParam)
        window.location.href = "/search/?query=" + myQueryParam;

    });

 
    $('#search_add_to_cart').click(function(){
        $.ajax({
            url: "/search/",
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