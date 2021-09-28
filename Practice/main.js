//DOM elements
const time = document.getElementById('time'),
    greeting = document.getElementById('greeting'),
    name = document.getElementById('name'),
    focus = document.getElementById('focus');

//Show Time
    function showTime(){
        let today = new Date(),
            hour =  today.getHours(),
            min = today.getMinutes(),
            sec = today.getSeconds();

        const amPM = hour>=12 ? 'PM' : 'AM';

        //12hr Format
        hour =  hour%12 || 12;

        time.innerHTML = '${hour}<span>:</span>${addZero(min)}<span>:</span>${addZero(sec)}' ;

        setTimeout(showTime,1000);
    }

    //Add Zeros
    function addZero(n){
        return (parseInt(n,10) < 10 ? '0' : '') +n;
    }

    // Set Background and Greeting
    function setBgGreet() {
        let today = new Date(),
            hour = today.getHours();
        //if(hour<12){
          //  document.body.style.backgroundImage = "url('')";
            //greeting.textContent = 'Goodmorning'
      //  }
    
    }

    //Get Name
    function getName(){
        if(localStorage.getItem('name')==null){
            name.textContent = '[Enter Name]';
        }else{
            focus.textContent = localStorage.getItem('name');
        }
    }

    //Set Name
    function setName(e) {
        if(e.type === 'keypress'){
            if(e.which == 13 || e.keyCode == 13) {
                localStorage.setItem('name', e.target.innerText);
                name.blur();
            }

        }else {
            localStorage.setItem('name', e.target.innerText);
        }
        }
    }

    name.addEventListener('keypress',setName);
    name.addEventListener('blur',setName);


    showTime()
    setBgGreet()