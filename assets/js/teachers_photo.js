import $ from 'jquery';
import 'owl.carousel2/dist/owl.carousel.min.js';


$(document).ready(function(){
  let teacher_carousel = $('.teacher-photo-carousel');
  teacher_carousel.owlCarousel({
    items: 1,
    loop: true,
    autoplay: true,
    autoplayTimeout:2000,
    dots: false,
  });

  teacher_carousel.trigger('stop.owl.autoplay');
  $('.course').on('mouseover',function(e){
    teacher_carousel.trigger('play.owl.autoplay');
  });
  $('.course').on('mouseleave',function(e){
    teacher_carousel.trigger('stop.owl.autoplay');
  })
});