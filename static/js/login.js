document.addEventListener("DOMContentLoaded", function () {
    var form = document.getElementById("login-form");

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        var email = document.getElementById("email").value.trim();
        var password = document.getElementById("password").value.trim();
        var isValid = true;

        if (email === "") {
            document.getElementById("email-error").textContent = "Please enter your email.";
            document.getElementById("email").classList.add("is-invalid");
            isValid = false;
        } else {
            document.getElementById("email-error").textContent = "";
            document.getElementById("email").classList.remove("is-invalid");
        }

        if (password === "") {
            document.getElementById("password-error").textContent = "Please enter your password.";
            document.getElementById("password").classList.add("is-invalid");
            isValid = false;
        } else {
            document.getElementById("password-error").textContent = "";
            document.getElementById("password").classList.remove("is-invalid");
        }

        if (isValid) {
            console.log("Form is valid. Submitting...");
            form.submit();
        } else {
            console.log("Form is not valid. Please fill in all fields.");
        }
    });
});
