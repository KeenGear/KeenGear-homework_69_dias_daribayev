$(function () {
    $('#calculator-form').on('submit', function (e) {
        e.preventDefault();
    });
    $('.calculator-btn').on('click', function () {
        var operation = $(this).data('operation');
        var formData = $('#calculator-form').serialize();
        $.ajax({
            url: '/api/' + operation + '/',
            method: 'POST',
            data: formData,
            success: function (data) {
                $('.result').html('<span class="success">' + data.answer + '</span>');
            },
            error: function (jqXHR, textStatus, errorThrown) {
                $('.result').html('<span class="error">' + jqXHR.responseJSON.error + '</span>');
            }
        });
    });
});
