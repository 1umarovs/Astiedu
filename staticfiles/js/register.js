$(function() {
    // Initialize form validation on the registration form.
    // It has the name attribute "registration"
    $("form[name='registration']").validate({
        // Specify validation rules
        rules: {
            name: "required",
            email: {
                required: true,
                email: true
            },
            password: {
                required: true,
                minlength: 5
            },
            password_confirmation: {
                required: true,
                equalTo: "#password"
            }
        },
        // Specify validation error messages
        messages: {
            name: full_name,
            password: {
                required: password,
                minlength: password_length
            },
            email: email,
            password_confirmation: {
                required: password_confirmation,
                equalTo: password_confirmation_check
            }
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
    });
});
