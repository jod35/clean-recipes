const nav = document.querySelector("header");
const logo = document.querySelector(".logo");
const nav_bar = document.querySelector(".nav-bar");

window.onscroll = function () {
  shrinkMyNav();
};

function shrinkMyNav() {
  if (
    document.body.scrollTop > 100 ||
    document.documentElement.scrollTop > 100
  ) {
    nav_bar.getElementsByClassName.padding = "5px";
    logo.getElementsByClassName.padding = "5px";
    nav.style.height = "50px";
  } else {
    nav.style.height = "80px";
  }
}
