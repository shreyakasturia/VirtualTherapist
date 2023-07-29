const dfMessenger = document.querySelector('df-messenger');

dfMessenger.addEventListener('df-response-received', function (event) {
    sessionID = dfMessenger.getAttribute("session-id");

    console.log(sessionID);
    console.log("received");
    console.log(event);

    var displayName = event.detail.response.queryResult.intent.displayName;

    displayName = displayName.replaceAll(" ", "_");
    displayName = displayName.replaceAll("/", "_");
    console.log(displayName);
    var video_folder = "/videos/";
    var videoURL = video_folder + displayName + ".mp4";
    changeVid(videoURL);
});

function switchToIdle() {
    var myVideo = document.getElementById("myVideo");
    var idleVideo = document.getElementById("idleVideo");
  
    myVideo.style.display = "none";
    myVideo.muted = true;
    idleVideo.style.display = "block";
  
    idleVideo.play();
  }
}


function changeVid(URL) {
    var vid = document.getElementById("myVideo");
    vid.src = URL;
    vid.load();
    vid.play();
    document.getElementById("myVideo").style.opacity = "1";
    document.getElementById("idleVideo").style.opacity = "0";
}

function redirectPage() {
    var url = "https://ufl.qualtrics.com/jfe/form/SV_ey59qVuNUXXcKh0"
    window.open(url);
}