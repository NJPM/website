require('dotenv').config()

jQuery(document).ready(function($){
    if (sessionStorage.getItem('over18') !== 'true') {
        $('#darkContent').hide();
        $('#adult').show();
    }else{
        $('#darkContent').show();
        $('#adult').hide();
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

    if (window.location.hash == "#darkRef/") {
        $('#collapseDarkRef').collapse();
    };
});


function startTimeout($) {
    let passwordAttempt = window.prompt('Password');
    if (passwordAttempt == process.env.CONTROLS_PW) {
        let timeoutLength = parseInt(window.prompt('Put hroar in timeout for how many minutes?', '15'));
        if (Number.isInteger(timeoutLength)) {
            var request = new XMLHttpRequest();
            request.open('POST', 'https://api.pushbullet.com/v2/pushes');
            request.setRequestHeader('Access-Token', process.env.PUSH_BULLET_TOKEN);
            request.send({type: "note", title: "timeout"});
            window.alert(`${timeoutLength}-minute timeout sent.`);
        }
        else {
            window.alert('Please enter a whole number.');
        }
    }
    else {
        window.alert('Incorrect password.')
    }
}
