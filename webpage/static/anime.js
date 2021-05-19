// Wrap every letter in a span
var textWrapper = document.getElementById("letters");
textWrapper.innerHTML = textWrapper.textContent.replace(/\S/g, "<span class='letter'>$&</span>");
anime.timeline({loop: true})
  .add({
    targets: '.banner-area .letter',
    scale: [4,1],
    opacity: [0,1],
    translateZ: 0,
    easing: "easeOutExpo",
    duration: 950,
    delay: (el, i) => 70*i
  }).add({
    targets: '.banner-area .letter',
    opacity: .2,
    duration: 1000,
    easing: "easeOutExpo",
    delay: 1000

  });