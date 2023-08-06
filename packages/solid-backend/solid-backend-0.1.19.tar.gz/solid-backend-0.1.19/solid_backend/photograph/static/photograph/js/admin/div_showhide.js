function checkFields(){
    if( $('#id_format_0').prop("checked")){
        $('#id_img_alt').show();
    }else{
        $('#id_img_alt').hide();
    }
}

$(document).ready( function() {
    $('#id_format').click(function(){
        checkFields();
    });
    checkFields();
});
