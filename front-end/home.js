function hideAlerts() {
    document.getElementById("currentAlertYellow").style.display = "none";
    document.getElementById("currentAlertOrange").style.display = "none";
    document.getElementById("currentAlertRed").style.display = "none";
    document.getElementById("currentAlertBlack").style.display = "none";
}

function hideAllAlerts() {
    document.getElementById("currentAlertGreen").style.display = "none";
    hideAlerts();
}

document.addEventListener("DOMContentLoaded", function() {
	hideAlerts();
});

$(document).ready(function () {
    var update = function () {
        $('#serializearray').text(
            JSON.stringify($('form').serializeArray())
        );
        $('#serialize').text(
            JSON.stringify($('form').serialize())
        );
    };
    update();
    $('form').change(update);
});

$(document).ready(function () {
    $('#changeGAlert').click(function () {
        changePage("currentAlertGreen", "#BDDE8D")
    });

    $('#changeYAlert').click(function () {
        changePage("currentAlertYellow", "#ffffa5")
    });

    $('#changeOAlert').click(function () {
        changePage("currentAlertOrange", "#e59544")
    });

    $('#changeRAlert').click(function () {
        changePage("currentAlertRed", "#990000");
    });

    $('#changeBAlert').click(function () {
        changePage("currentAlertBlack", "black")
    });
});

function changePage(elementId, backgroundColor) {
    hideAllAlerts();
    document.getElementById(elementId).style.display = "block";
    document.body.style.backgroundColor = backgroundColor;
}

function alertUser(distance) {
    if(distance < 10) {
        changePage("currentAlertBlack", "black");
    } else if(distance >= 10 && distance < 50) {
        changePage("currentAlertRed", "#990000");
    } else {
        changePage("currentAlertGreen", "#BDDE8D");
    }
}

document.addEventListener('DOMContentLoaded', bindButtons);

function bindButtons() {
    document.getElementById('sub').addEventListener('click', function (event) {
        var req = new XMLHttpRequest();
        var payload = { data: null };    
        payload.data = "latitude=" + document.getElementById('lat').value + "&longitude=" + document.getElementById('long').value;
        var url = "http://vps54981.vps.ovh.ca:8080/?" + payload.data;
        console.log(url);

        req.open('GET', url, true);
        req.addEventListener('load', function () {
            if (req.status >= 200 && req.status < 400) {
                var response = JSON.parse(req.responseText);
                if(response.activeAlert === true) {
                    alertUser(response.distance);
                } else {
                    changePage("currentAlertGreen", "#BDDE8D");
                }
            } else {
                console.log("Error in network request: " + request.statusText);
            }
        });
        req.send(null);
        event.preventDefault();
    });
}
