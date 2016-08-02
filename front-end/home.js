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
        hideAlerts();
        document.getElementById("currentAlertGreen").style.display = "block";
        document.body.style.backgroundColor = "#BDDE8D";
    });

    $('#changeYAlert').click(function () {
        hideAllAlerts();
        document.getElementById("currentAlertYellow").style.display = "block";
        document.body.style.backgroundColor = "#ffffa5";
    });

    $('#changeOAlert').click(function () {
        hideAllAlerts();
        document.getElementById("currentAlertOrange").style.display = "block";
        document.body.style.backgroundColor = "#e59544";
    });

    $('#changeRAlert').click(function () {
        hideAllAlerts();
        document.getElementById("currentAlertRed").style.display = "block";
        document.body.style.backgroundColor = "#990000";
    });

    $('#changeBAlert').click(function () {
        hideAllAlerts();
        document.getElementById("currentAlertBlack").style.display = "block";
        document.body.style.backgroundColor = "black";
    });
});

document.addEventListener('DOMContentLoaded', bindButtons);

function bindButtons() {
    document.getElementById('sub').addEventListener('click', function (event) {
        var req = new XMLHttpRequest();
        var payload = { data: null };
        payload.data = document.getElementById('lat').value + "&" + document.getElementById('long').value;
        console.log(payload.data);
        var url = "http://localhost:58639/index.html?" + payload.data;
        req.open('GET', url, true);
        req.addEventListener('load', function () {
            if (req.status >= 200 && req.status < 400) {
                alert("Latitude and Longtitude sent");
            } else {
                console.log("Error in network request: " + request.statusText);
            }
        });
        req.send(JSON.stringify(payload));
        event.preventDefault();
    });
}
