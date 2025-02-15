




// Wait for the DOM to load
document.addEventListener("DOMContentLoaded", function () {
    // Check if we are on the login page
    const loginContainer = document.querySelector(".login-box");

    if (loginContainer) {
        // Inject the video into the body
        const video = document.createElement("video");
        video.autoplay = true;
        video.muted = true;
        video.loop = true;
        video.id = "background-video";

        // Check screen size and load different video
        const videoSource = document.createElement("source");
        if (window.innerWidth < 768) {
            // Mobile video
            videoSource.src = "/static/videos/People Working in Office - Busy Day - Royalty Free Stock Video.mp4";  // Mobile video path

        } else {
            // Desktop video
            videoSource.src = "/static/videos/Business Man Walking(1080p).mp4";  // Desktop video path

        }

        videoSource.type = "video/mp4";
        video.appendChild(videoSource);

        // Add an event listener to restart the video if loop fails
        video.addEventListener("ended", function () {
            video.currentTime = 0;
            video.play();
        });

        // Style the video
        video.style.position = "fixed";
        video.style.top = "0";
        video.style.left = "0";
        video.style.width = "100vw";
        video.style.height = "100vh";
        video.style.objectFit = "cover";
        video.style.zIndex = "-1";

        // Inject the video into the body
        document.body.prepend(video);
    }
});
