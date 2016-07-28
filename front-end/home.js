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