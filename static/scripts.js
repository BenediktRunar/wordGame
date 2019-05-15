$(document).ready(function() {

    console.log("script connected");

    var strLen = 0;

    $('.letterBox').on('click', function(event) {

        var squareSelected = $(this);
        console.log(squareSelected.find('h1')[0].innerText);
    });

});