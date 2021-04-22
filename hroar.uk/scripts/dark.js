jQuery(document).ready(function($){
    if (sessionStorage.getItem('over18') !== 'true') {
        $('#darkContent').hide();
        $('#adult').show();
    }else{
        $('#darkContent').show();
    }

    $('#enter').on('click',function(){
        $('#adult').hide();
        $('#darkContent').show();
        sessionStorage.setItem('over18', 'true');
    });

    $('#leave').on('click',function(){
        window.location.replace("/");
        sessionStorage.setItem('over18', '');
    });
});
