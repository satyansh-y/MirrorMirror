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

        ws.onopen = function(evt) {
            $("#ws-status").html("Connected");
            };

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

        $("#Send").click(function(){
            var Green= $("#Green_slider").value;
            var Red= $("#Red_slider").value;
            var Blue= $("#Blue_slider").value;
            Green = String(Green);
            Blue = String(Blue);
            Red = String(Red);

             ws.send("Send " + Red + " " + Green + " " + Blue);
            });


      });
