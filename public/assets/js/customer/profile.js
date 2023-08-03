$(document).ready(function () {
    $('#change_password').click(function(event){
        event.preventDefault();
        if (!$('#old').val()){
            $('#password_error').text('Please enter old password');
            $('#password_error_div').show();
            setTimeout(function(){
               $('#password_error_div').hide();
            }, 3000);
        }else if (!$('#new').val()){
            $('#password_error').text('Please enter new password');
            $('#password_error_div').show();
            setTimeout(function(){
               $('#password_error_div').hide();
            }, 3000);
        }else if (!$('#re_enter').val()){
            $('#password_error').text('Please enter reenter password');
            $('#password_error_div').show();
            setTimeout(function(){
               $('#password_error_div').hide();
            }, 3000);
        }
        else if ($('#new').val() !== $('#re_enter').val()){
            $('#password_error').text('New & Reenter passwords should be same');
            $('#password_error_div').show();
            setTimeout(function(){
               $('#password_error_div').hide();
            }, 3000);
        }
        else{
            $.ajax({
                url: "/user/change-password/",
                type : "POST",
                data: {
                    'old': $('#old').val(),
                    'new': $('#new').val(),
                    'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
                },
                success: function (data) {
                    if(data.status == 'success'){
                        $('#password_error').text(data.message);
                        $('#password_error_div').show();
                        setTimeout(function(){
                           $('#password_error_div').hide();
                           window.location.href = '/';
                        }, 1000);
                    }else{
                        $('#password_error').text(data.message);
                        $('#password_error_div').show();
                        setTimeout(function(){
                           $('#password_error_div').hide();
                        }, 3000);
                    }
                }
            });
        }
    });
});