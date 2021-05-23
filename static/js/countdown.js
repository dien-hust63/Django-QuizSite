
const countdownBox = document.getElementById('countdown');
console.log(countdownBox.title)

function startTimer(duration,display) {
    var timer = parseInt(duration, 10) * 60;
    var minutes, seconds;

    var countdown = setInterval(function () {
        
        minutes = Math.floor(timer / 60);
        seconds = timer % 60;
        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;
        console.log(timer);
        timer = timer - 1;
        
        if (timer < 0) {
            display.textContent = "Time out ."
            clearInterval(countdown);
            // $(document).ready(function(){
            //     $('#form1').submit(function(){
            //         $.ajax({
            //             url : 'inserir.php',
            //             type : 'POST',
            //             data : $('form').serialize(),
            //             success: function(data){
            //                 $('#resultado').html(data);
            //             }
            //         });
            //         return false;
            //     });
            // })
        }
    }, 1000);


    
}

startTimer(countdownBox.title, countdownBox)