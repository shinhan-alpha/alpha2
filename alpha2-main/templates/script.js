const menuBarContainer = document.querySelector(".menu-bar-container");
const menuBars = menuBarContainer.querySelectorAll(".menu-bar");
let isDragging = false;
let previousX;

menuBars[0].addEventListener("mousedown", (e) => {
  isDragging = true;
  previousX = e.clientX;
});

menuBars[0].addEventListener("mousemove", (e) => {
  if (isDragging) {
    const delta = e.clientX - previousX;
    const left = parseInt(window.getComputedStyle(menuBarContainer).getPropertyValue("left"));
    const width = parseInt(window.getComputedStyle(menuBarContainer).getPropertyValue("width"));
    const containerWidth = menuBarContainer.clientWidth;
    const maxLeft = containerWidth - width;
    const newLeft = Math.min(0, Math.max(left + delta, maxLeft));
    menuBarContainer.style.left = `${newLeft}px`;
    previousX = e.clientX;
  }
});

menuBars[0].addEventListener("mouseup", () => {
  isDragging = false;
});

function toggleMenu(index) {
  for (let i = 0; i < menuBars.length; i++) {
    if (i === index) {
      menuBars[i].classList.add("active");
    } else {
      menuBars[i].classList.remove("active");
    }
  }
}

for (let i = 0; i < menuBars.length; i++) {
  menuBars[i].addEventListener("click", () => {
    toggleMenu(i);
  });
}

toggleMenu(0);