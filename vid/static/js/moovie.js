let videoContainer = document.querySelector(".video-container");
let container = document.querySelector(".container");
let myVideo = document.getElementById("my-video");
let rotateContainer = document.querySelector(".rotate-container");
let videoControls = document.querySelector(".controls");
let playButton = document.getElementById("play-btn");
let pauseButton = document.getElementById("pauseButton");
let volume = document.getElementById("volume");
let volumeRange = document.getElementById("volume-range");
let volumeNum = document.getElementById("volume-num");
let high = document.getElementById("high");
let low = document.getElementById("low");
let mute = document.getElementById("mute");
let sizeScreen = document.getElementById("size-screen");
let screenCompress = document.getElementById("screen-compress");
let screenExpand = document.getElementById("screen-expand");
const currentProgress = document.getElementById("current-progress");
const currentTimeRef = document.getElementById("current-time");
const maxDuration = document.getElementById("max-duration");
const progressBar = document.getElementById("progress-bar");
const playbackSpeedButton = document.getElementById("playback-speed-btn");
const playbackContainer = document.querySelector(".playback");
const playbackSpeedOptions = document.querySelector(".playback-options");
const  uuid = JSON.parse(document.getElementById('uuid_json').textContent)
function slider() {
    valPercent = (volumeRange.value / volumeRange.max) * 100;
    volumeRange.style.background = `linear-gradient(to right, #FF00FFFF ${valPercent}%, #000000 ${valPercent}%)`;
}

//events object
let events = {
    mouse: {
        click: "click",
    },
    touch: {
        click: "touchstart",
    },
};

let deviceType = "";

//Detech touch device
const isTouchDevice = () => {
    try {
        //We try to create TouchEvent (it would fail for desktops and throw error)
        document.createEvent("TouchEvent");
        deviceType = "touch";
        return true;
    } catch (e) {
        deviceType = "mouse";
        return false;
    }
};

//play and pause button
playButton.addEventListener("click", () => {
    myVideo.play();
    pauseButton.classList.remove("hide");
    playButton.classList.add("hide");
    sendVideoState();
});

pauseButton.addEventListener(
    "click",
    (pauseVideo = () => {
        myVideo.pause();
        pauseButton.classList.add("hide");
        playButton.classList.remove("hide");
        sendVideoState();
    })
);

//playback
playbackContainer.addEventListener("click", () => {
    playbackSpeedOptions.classList.remove("hide");
});

//if user clicks outside or on the option
window.addEventListener("click", (e) => {
    if (!playbackContainer.contains(e.target)) {
        playbackSpeedOptions.classList.add("hide");
    } else if (playbackSpeedOptions.contains(e.target)) {
        playbackSpeedOptions.classList.add("hide");
    }
});

//playback speed
const setPlayback = (value) => {
    playbackSpeedButton.innerText = value + "x";
    myVideo.playbackRate = value;
};

//mute video
const muter = () => {
    mute.classList.remove("hide");
    high.classList.add("hide");
    low.classList.add("hide");
    myVideo.volume = 0;
    volumeNum.innerHTML = 0;
    volumeRange.value = 0;
    slider();
};

//when user click on high and low volume then mute the audio
high.addEventListener("click", muter);
low.addEventListener("click", muter);

//for volume
volumeRange.addEventListener("input", () => {
    //for converting % to decimal values since video.volume would accept decimals only
    let volumeValue = volumeRange.value / 100;
    myVideo.volume = volumeValue;
    volumeNum.innerHTML = volumeRange.value;
    //mute icon, low volume, high volume icons
    if (volumeRange.value < 50) {
        low.classList.remove("hide");
        high.classList.add("hide");
        mute.classList.add("hide");
    } else if (volumeRange.value > 50) {
        low.classList.add("hide");
        high.classList.remove("hide");
        mute.classList.add("hide");
    }
});

//Screen size
screenExpand.addEventListener("click", () => {
    screenCompress.classList.remove("hide");
    screenExpand.classList.add("hide");
    videoContainer
        .requestFullscreen()
        .catch((err) => alert("Your device doesn't support full screen API"));
    if (isTouchDevice) {
        let screenOrientation =
            screen.orientation || screen.mozOrientation || screen.msOrientation;
        if (screenOrientation.type === "portrait-primary") {
            //update styling for fullscreen
            pauseVideo();
            rotateContainer.classList.remove("hide");
            const myTimeout = setTimeout(() => {
                rotateContainer.classList.add("hide");
            }, 3000);
        }
    }
});

//if user presses escape the browser fire 'fullscreenchange' event
document.addEventListener("fullscreenchange", exitHandler);
document.addEventListener("webkitfullscreenchange", exitHandler);
document.addEventListener("mozfullscreenchange", exitHandler);
document.addEventListener("MSFullscreenchange", exitHandler);

function exitHandler() {
    //if fullscreen is closed
    if (
        !document.fullscreenElement &&
        !document.webkitIsFullScreen &&
        !document.mozFullScreen &&
        !document.msFullscreenElement
    ) {
        normalScreen();
    }
}

//back to normal screen
screenCompress.addEventListener(
    "click",
    (normalScreen = () => {
        screenCompress.classList.add("hide");
        screenExpand.classList.remove("hide");
        if (document.fullscreenElement) {
            if (document.exitFullscreen) {
                document.exitFullscreen();
            } else if (document.mozCancelFullScreen) {
                document.mozCancelFullScreen();
            } else if (document.webkitExitFullscreen) {
                document.webkitExitFullscreen();
            }
        }
    })
);

//Format time
const timeFormatter = (timeInput) => {
    let minute = Math.floor(timeInput / 60);
    minute = minute < 10 ? "0" + minute : minute;
    let second = Math.floor(timeInput % 60);
    second = second < 10 ? "0" + second : second;
    return `${minute}:${second}`;
};

//Update progress every second
setInterval(() => {
    currentTimeRef.innerHTML = timeFormatter(myVideo.currentTime);
    currentProgress.style.width =
        (myVideo.currentTime / myVideo.duration.toFixed(3)) * 100 + "%";
}, 1000);

//update timer
myVideo.addEventListener("timeupdate", () => {
    currentTimeRef.innerText = timeFormatter(myVideo.currentTime);
    maxDuration.innerText = timeFormatter(myVideo.duration);
});

//If user click on progress bar
isTouchDevice();
progressBar.addEventListener(events[deviceType].click, (event) => {
    //start of progressbar
    let coordStart = progressBar.getBoundingClientRect().left;
    //mouse click position
    let coordEnd = !isTouchDevice() ? event.clientX : event.touches[0].clientX;
    let progress = (coordEnd - coordStart) / progressBar.offsetWidth;
    //set width to progress
    currentProgress.style.width = progress * 100 + "%";
    //set time
    myVideo.currentTime = progress * myVideo.duration;
    sendVideoState();
    //play
    // myVideo.play();
    // pauseButton.classList.remove("hide");
    // playButton.classList.add("hide");
});

window.onload = () => {
    //display duration
    myVideo.onloadedmetadata = () => {
        maxDuration.innerText = myVideo.duration;
    };
    slider();
};
let mouseIdleTimer;
let controlsVisible = true;

// Function to hide controls
function hideControls() {
    if (controlsVisible) {
        document.querySelector(".controls").classList.add("hide");
        controlsVisible = false;
    }
}

// Function to show controls
function showControls() {
    if (!controlsVisible) {
        document.querySelector(".controls").classList.remove("hide");
        controlsVisible = true;
    }

    // Reset the timer for hiding controls
    clearTimeout(mouseIdleTimer);
    mouseIdleTimer = setTimeout(hideControls, 1500);
}

// Event listeners
document.addEventListener("mousemove", showControls);
document.addEventListener("keydown", showControls);

myVideo.addEventListener("play", showControls);
myVideo.addEventListener("pause", hideControls);
myVideo.addEventListener("ended", hideControls);
const socket = new WebSocket(
            'ws://'
            + window.location.host
            + '/ws/control/'
            + uuid
            + '/'
        );
// Listen for changes in video state from the server

socket.onmessage = (event) => {
    const parsedMessage = JSON.parse(event.data);
    if (parsedMessage.type === 'updateVideoState') {
        // Update the video state based on changes from the server
        updateVideoState(parsedMessage.data);
    } else {
        console.log(JSON.parse(event.data));
    }
};

// Function to update the video state and send it to the server
function updateVideoState(newState) {
        if (newState.isPlaying) {
        console.log('must play')
        myVideo.play();
        pauseButton.classList.remove("hide");
        playButton.classList.add("hide");
    } else {
        myVideo.pause();
        console.log('must pause')
        pauseButton.classList.add("hide");
        playButton.classList.remove("hide");
    }


    const currentTimeDifference = Math.abs(newState.currentTime - myVideo.currentTime);

    // Check if the time difference is within a small threshold (e.g., 0.1 seconds)
    if (currentTimeDifference < 0.1) {
        return;
    }

    myVideo.currentTime = newState.currentTime;

}

myVideo.addEventListener('seeked', () => {
    // Send the updated video state to the server when seeking occurs
    const newState = {
        currentTime: myVideo.currentTime,
        isPlaying: !myVideo.paused,
    };
    socket.send(JSON.stringify({type: 'updateVideoState', data: newState}));
});
window.addEventListener("beforeunload", () => {
    // Close the WebSocket connection before leaving the page
    socket.close();
});
function sendVideoState() {
    // Video state has changed
    const newState = {
        currentTime: myVideo.currentTime,
        isPlaying: !myVideo.paused, // true when playing, false when paused
    };
    socket.send(JSON.stringify({ type: 'updateVideoState', data: newState }));
}