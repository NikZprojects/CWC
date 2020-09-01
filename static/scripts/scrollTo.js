$(document).ready(function (){
    $("#jumpToRecipe").click(function (){
        $('html, body').animate({
            scrollTop: $("#recipe").offset().top
        }, 1500);
    });
});
