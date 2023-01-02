function generate_journey() {
    let genbutton = document.getElementById("genbutton");
    let textarea = document.getElementById("output");
    genbutton.innerHTML = "Generating...";
    let xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", "journey", false);
    xmlHttp.send();
    let journeydata = xmlHttp.responseText;
    if (journeydata.search('minutes') === -1) {
        console.log("failed: " + journeydata);
        journeydata = "This journey didn't work for some reason. I need to put the station id's in a list rather than the names to increase reliability, but until then just try generating a new journey.<br>Also, the server's internet connection could be down."
    }
    textarea.innerHTML = journeydata;
    genbutton.innerHTML = "Generate Journey";
}