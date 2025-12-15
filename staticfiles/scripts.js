document.getElementById("contactForm")?.addEventListener("submit", function(e) {
  e.preventDefault();
  alert("Thank you! Your message has been sent.");
  this.reset();
});


  const toggle = document.getElementById("menu-toggle");
    const navLinks = document.getElementById("nav-links");

    toggle.addEventListener("click", () => {
      navLinks.classList.toggle("open");
      toggle.classList.toggle("active");
    });