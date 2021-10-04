$('#discount_code_form').on('submit', function (e) {
    var form = $(this);
    var url ='http://127.0.0.1:8000/api/v1/account/discount'
    let discount_code = $('#discount_code').val()
    e.preventDefault();
    $.ajax({
        type: "POST",
        url: url,
        data: JSON.stringify({
            'discount_code': discount_code,
        }),
        success: function (data) {
            $("#final_price").html(data['final_price'])
            $("#discount").html(data['discount'])
            $("#discount").append('%')

        },
        error: function (xhr, errmsg, err) {
            $("#error_text").html('discount code is not valid')

        },
        contentType: "application/json",
        dataType: 'json',
    });
});