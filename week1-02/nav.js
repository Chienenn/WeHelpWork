let menuIcon = document.getElementById("menu-icon");
let mobileNav = document.querySelector(".mobile-nav");

menuIcon.addEventListener("click", function () {
  mobileNav.classList.toggle("show");
});
