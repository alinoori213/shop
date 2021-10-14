$('#register_form').on('submit', function (e) {
    let user_name = $('#id_username').val()
    let password = $('#id_password').val()
    let email = $('#id_email').val()
    let password2 = $('#id_confirm_password').val()
    e.preventDefault();
    $.ajax({
        type: "POST",
        url: 'http://127.0.0.1:8000/en/api/customer/',
        data: JSON.stringify({
            user_name: user_name,
            password: password,
            email: email,
            password2: password2
        }),
        success: function (data) {
            alert(data['username'] + ' ' + 'register is success')
            $('#non-field-error').html(' ')
        },
        error: function (xhr, errmsg, err) {
            console.log(JSON.parse(xhr.responseText))
            let non_field_errors = JSON.parse(xhr.responseText)
            $('#non-field-error').html(non_field_errors['non_field_errors'])
            $('#password-error').html(non_field_errors['password'])
            $('#confirm-password-error').html(non_field_errors['confirm_password'])
            $('#register_form').click(function () {
                $('#password-error').html('') ;
                $('#confirm-password-error').html('')
            });

        },
        contentType: "application/json",
        dataType: 'json',
    });
});