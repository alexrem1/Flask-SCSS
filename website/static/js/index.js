// mobile nav
const hamburgerContainer = document.querySelector(".hamburger");
const hamburger = document.querySelectorAll(".hamburger__btn");
const menu = document.querySelector(".nav");
let showMenu = false;

hamburgerContainer.addEventListener("click", toggleMenu);

function toggleMenu(e) {
  hamburger.forEach((item) => item.classList.toggle("open"));
  menu.classList.toggle("open");
  hamburgerContainer.classList.toggle("open");

  if (document.querySelector(".dropdown")) {
    if (e.target.classList.contains("open")) {
      document.querySelector(".dropdown").classList.remove("open");
      document.querySelector(".arrow").classList.remove("active");
    }
  }
}

//dropdown nav
const dropdown = document.querySelector(".dropdown");
const arrow = document.querySelector(".arrow");

if (dropdown) {
  dropdown.addEventListener("click", () => {
    dropdown.classList.toggle("open");
    arrow.classList.toggle("active");
  });
}

// dropdown comments
const viewComments = document.getElementsByClassName("viewComments");
const postsComments = document.getElementsByClassName("posts__comments");

for (let i = 0; i < viewComments.length; i++) {
  viewComments[i].addEventListener("click", function () {
    if (postsComments.length > 0) {
      postsComments[i].classList.toggle("open");
    }
  });
}

//active nav element FIXXXXX
const navLinks = document.getElementsByClassName("nav__item");

for (let i = 0; i < navLinks.length; i++) {
  navLinks[i].addEventListener("click", function (e) {
    if (navLinks.length > 0) {
      if (!e.target.classList.contains("active")) {
        navLinks[i].classList.add("active");
      }
      this.classList += " active";
    }
  });
}

// form focus
const formFocus = document.querySelector(".form-focus");

window.addEventListener("load", (e) => {
  if (formFocus) {
    formFocus[0].focus();
  }
});

//close alert
const flaskAlert = document.querySelector(".alert");
const closeAlert = document.querySelector(".close");

window.addEventListener("load", (e) => {
  if (flaskAlert) {
    closeAlert.addEventListener("click", (e) => {
      if (e.target.className === "close") {
        flaskAlert.classList.add("hide");
      }
    });
  }
});
