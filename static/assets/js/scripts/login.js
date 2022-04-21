$(document).ready(function () {
    $("#login-form").validate({
        rules: {
            username: { required: true },
            password: { required: true }
        },
        submitHandler: function(form, event) {
            form.submit();
        }
    });

    $("#register-form").validate({
        rules: {
            username: { required: true },
            password: { required: true }
        },
        submitHandler: function(form, event) {
            form.submit();
        }
    });
});