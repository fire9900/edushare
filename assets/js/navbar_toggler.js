let page = document.querySelector(".page");
let navbar_toggler = document.querySelector(".navbar-toggler");
page.setAttribute('navbar-toggler_visible', window.location.pathname == '/');

if (window.location.pathname == '/') {navbar_toggler.style.display = 'none'}


document.querySelector(".navbar-toggler__btn").onclick = () => {
	page.setAttribute('navbar-toggler_visible', !(page.getAttribute('navbar-toggler_visible') == 'true'));
};