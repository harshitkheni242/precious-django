const bar = document.getElementById('bar');
const close = document.getElementById('close');
const nav = document.getElementById('navbar');

if(bar) {
    bar.addEventListener('click', () => {
        nav.classList.add('active');
    })
}

if(close) {
    close.addEventListener('click', () => {
        nav.classList.remove('active');
    })
}
const slides = document.querySelectorAll('.slide');
            let currentSlide = 0;
      
            function showSlide() {
              // Hide all slides except the current one
              slides.forEach((slide, index) => {
                if (index === currentSlide) {
                  slide.classList.add('active');
                } else {
                  slide.classList.remove('active');
                }
              });
      
              // Move to the next slide
              currentSlide++;
              if (currentSlide >= slides.length) {
                currentSlide = 0;
              }
      
              // Schedule the next slide to be shown
              setTimeout(showSlide, 5000);
            }
      
            // Show the first slide
            showSlide();




var MainImg = document.getElementById("MainImg");
var smallimg = document.getElementsByClassName("small-img");

smallimg[0].onclick = function(){
    MainImg.src = smallimg[0].src;
}
smallimg[1].onclick = function(){
    MainImg.src = smallimg[1].src;
}
smallimg[2].onclick = function(){
    MainImg.src = smallimg[2].src;
}
smallimg[3].onclick = function(){
    MainImg.src = smallimg[3].src;
}
        
