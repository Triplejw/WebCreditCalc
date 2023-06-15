$(document).ready(function() {
    // Adjust the height of the background animation element
    var windowHeight = $(window).height();
    $('#background-animation').height(windowHeight);

    // Reset the form when the reset button is clicked
    $('#reset-button').click(function() {
        $('#credit-calculator-form')[0].reset();
    });
});
