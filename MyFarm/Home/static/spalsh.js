document.addEventListener("DOMContentLoaded", function() {
    const splash = document.getElementById("splash");
    const mainContent = document.getElementById("main-content");
    const enterButton = document.getElementById("enter-button");

    enterButton.addEventListener("click", function() {
        splash.style.display = "none";
        mainContent.style.display = "block";
    });
});
