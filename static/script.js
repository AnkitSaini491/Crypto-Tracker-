
// =========================
// Crypto Tracker JS
// =========================

// Search Coins
const search = document.getElementById("search");

if (search) {

search.addEventListener("keyup", () => {

let value = search.value.toLowerCase();

let cards = document.querySelectorAll(".card");

cards.forEach(card => {

let name = card.querySelector("h2").innerText.toLowerCase();

let symbol = card.querySelector("h4").innerText.toLowerCase();

if(name.includes(value) || symbol.includes(value)){

card.style.display="block";

}else{

card.style.display="none";

}

});

});

}

// Auto Refresh Every 30 Seconds

setInterval(()=>{

location.reload();

},30000);


// Fade Animation

const cards=document.querySelectorAll(".card");

const observer=new IntersectionObserver(entries=>{

entries.forEach(entry=>{

if(entry.isIntersecting){

entry.target.style.opacity="1";

entry.target.style.transform="translateY(0)";

}

});

});

cards.forEach(card=>{

card.style.opacity="0";

card.style.transform="translateY(40px)";

card.style.transition=".6s";

observer.observe(card);

});


// Scroll Navbar Effect

window.addEventListener("scroll",()=>{

const nav=document.querySelector("nav");

if(window.scrollY>30){

nav.style.boxShadow="0 5px 20px rgba(0,0,0,.4)";

}else{

nav.style.boxShadow="none";

}

});


// Loading Animation

window.onload=()=>{

document.body.style.opacity="1";

};

document.body.style.opacity="0";

document.body.style.transition=".5s";


// Coin Card Hover Sound (Optional)

cards.forEach(card=>{

card.addEventListener("mouseenter",()=>{

card.style.transform="translateY(-10px) scale(1.03)";

});

card.addEventListener("mouseleave",()=>{

card.style.transform="translateY(0)";

});

});
