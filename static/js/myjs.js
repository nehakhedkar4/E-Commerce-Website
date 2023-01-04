console.log("Script loaded");

console.log("script");
$('.owl-carousel').owlCarousel({
    
    loop:true,
    margin:20,
    nav:false,
    dots:false,
    autoplay:true,
    autoplayTimeout:2000,
    autoplayHoverPause:true,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:4
        }
    }
})
console.log("inside")
// $('.qty').on('click', function(e){
//     e.preventDefault();
//     $(this).css('border-color', 'red');
//   });
