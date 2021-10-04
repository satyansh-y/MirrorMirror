$(document).ready(function(){
    
    var WEBSOCKET_ROUTE = "/ws";

    if(window.location.protocol == "http:"){
        //localhost
        var ws = new WebSocket("ws://" + window.location.host + WEBSOCKET_ROUTE);
        }
    else if(window.location.protocol == "https:"){
        //Dataplicity
        var ws = new WebSocket("wss://" + window.location.host + WEBSOCKET_ROUTE);
        }
    ws.onmessage = function(evt) {
        message = JSON.parse(evt.data);
        console.log(message);
        };
    // DOM Elements
    const time = document.getElementById('time'),
        greeting = document.getElementById('greeting'),
        name = document.getElementById('name'),
        focus = document.getElementById('focus'),
        on = document.getElementById('b_on'),
        off = document.getElementById('b_off');

    // Options
    const showAmPm = true;

    // Show Time
    function showTime() {
    let today = new Date(),
        hour = today.getHours(),
        min = today.getMinutes(),
        sec = today.getSeconds();

    // Set AM or PM
    const amPm = hour >= 12 ? 'PM' : 'AM';

    // 12hr Format
    hour = hour % 12 || 12;

    // Output Time
    time.innerHTML = `${hour}<span>:</span>${addZero(min)}<span>:</span>${addZero(
        sec
    )} ${showAmPm ? amPm : ''}`;

    setTimeout(showTime, 1000);
    }

    // Add Zeros
    function addZero(n) {
    return (parseInt(n, 10) < 10 ? '0' : '') + n;
    }


    // Get Name
    function getName() {
    if (localStorage.getItem('name') === null) {
        name.textContent = '[Enter Name]';
    } else {
        name.textContent = localStorage.getItem('name');
    }
    }

    // Set Name
    function setName(e) {
    if (e.type === 'keypress') {
        // Make sure enter is pressed
        if (e.which == 13 || e.keyCode == 13) {
        localStorage.setItem('name', e.target.innerText);
        name.blur();
        }
    } else {
        localStorage.setItem('name', e.target.innerText);
    }
    }

    function turnOn(a){
        document.getElementById("b_on").style.backgroundColor = '#4CAF50';
        document.getElementById("b_off").style.backgroundColor = '#444744';
    }
    function turnOff(a){
        document.getElementById("b_on").style.backgroundColor = '#444744';
        document.getElementById("b_off").style.backgroundColor = '#4CAF50';
    }
    
    on.addEventListener('click',turnOn);
    off.addEventListener('click',turnOff);
    name.addEventListener('keypress', setName);
    name.addEventListener('blur', setName);
    showTime();
    getName();

    ws.onmessage = function(evt) {
    };

    ws.onclose = function(evt) {
        $("#ws-status").html("Disconnected");
        };

    $("#b_on").click(function(){
        ws.send("ON");
        });

    $("#b_off").click(function(){
        ws.send("OFF");
        });

    $("#green").click(function(){
        ws.send("Green");
        });

    $("#red").click(function(){
        ws.send("Red");
        });

        $("#blue").click(function(){
        ws.send("Blue");
        });

    $("#white").click(function(){
        ws.send("White");
        });

    $("#yellow").click(function(){
        ws.send("Yellow");
        });            

    $("#purple").click(function(){
        ws.send("Purple");
        });

    // Run
        
});