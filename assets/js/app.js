import AOS from 'aos'

AOS.init();

document.querySelector(".content").setAttribute('on_index', window.location.pathname == '/');