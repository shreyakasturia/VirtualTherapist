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


function playVideo() {
  var myVideo = document.getElementById("myVideo");
  myVideo.play()
}

function switchToIdle() {
  var myVideo = document.getElementById("myVideo");
  var idleVideo = document.getElementById("idleVideo");

  myVideo.pause(); 
  myVideo.style.display = "none";
  idleVideo.style.display = "block";

  idleVideo.play();
}