import $ from 'jquery';
import 'owl.carousel2/dist/owl.carousel.min.js';


$(document).ready(function(){
  $('.teachers-carousel').owlCarousel({
    nav: true,
    loop: true,
    autoWidth: true,
    margin: 50,
    navText : ["<i class='fa fa-chevron-left'></i>","<i class='fa fa-chevron-right'></i>"],
  });
});