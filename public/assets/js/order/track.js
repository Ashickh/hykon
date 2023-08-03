


function showTextArea() {
    var selectBox = document.getElementById("cancelReasonInput");
    var textArea = document.getElementById("specify-reason-section");
    if (selectBox.value === "Others") {
        textArea.style.display = "block";
    } else {
        textArea.style.display = "none";
    }
}
function clearSelect() {
    var selectBox = document.getElementById("cancelReasonInput");
    selectBox.value = "";
}

