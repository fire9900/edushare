import $ from 'jquery';
import 'owl.carousel2/dist/owl.carousel.min.js';


$(document).ready(function(){
  $('.owl-carousel').owlCarousel({
    loop: true,
    autoWidth: true,
    margin: 50,
  });
});