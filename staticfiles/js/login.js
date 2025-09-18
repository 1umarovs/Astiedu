$(function() {
    // Initialize form validation on the registration form.
    // It has the name attribute "registration"
    $("form[name='login']").validate({
        // Specify validation rules
        rules: {
            email: {
                required: true,
                email: true
            },
            password: {
                required: true,
                minlength: 5
            },
        },
        // Specify validation error messages
        messages: {
            password: {
                required: password,
                minlength: password_length
            },
            email: email,
        },
        // Highlight invalid fields on hover
        highlight: function(element) {
            $(element).addClass('border-danger');
        },
        unhighlight: function(element) {
            $(element).removeClass('border-danger');
        },
        // Make sure the form is submitted to the destination defined
        // in the "action" attribute of the form when valid
        submitHandler: function(form) {
            form.submit();
        }
    });

    // Validate fields on hover
    $("input").on("blur", function() {
        $(this).valid();
        // if (!$(this).valid()) {
        //     $(this).addClass('border-danger').removeClass("border-success");
        // } else {
        //     $(this).removeClass('border-danger').addClass('border-success');
        // }
    });
});
