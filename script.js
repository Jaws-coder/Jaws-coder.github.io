// Authentication function
function authenticate() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  const errorMsg = document.getElementById("error-msg");

  if (username === "Poopy" && password === "Head") {
    document.getElementById("auth-screen").style.display = "none";
    document.getElementById("content").style.display = "block";
  } else {
    errorMsg.style.display = "block";
  }
}

// Fullscreen image viewing functions
function openFullscreen(index) {
  const fullscreen = document.getElementById("fullscreen");
  const fullscreenImg = document.getElementById("fullscreen-img");

  const images = document.querySelectorAll(".image-block img");
  fullscreenImg.src = images[index].src;
  fullscreen.style.display = "flex";
}

function closeFullscreen() {
  document.getElementById("fullscreen").style.display = "none";
}

function changeSlide(direction) {
  const images = document.querySelectorAll(".image-block img");
  const fullscreenImg = document.getElementById("fullscreen-img");
  let currentIndex = Array.from(images).findIndex(img => img.src === fullscreenImg.src);

  currentIndex = (currentIndex + direction + images.length) % images.length;
  fullscreenImg.src = images[currentIndex].src;
}
