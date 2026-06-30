// =========================
// Crypto Tracker Script
// =========================

// Search Function

const search = document.getElementById("search");

if(search){

search.addEventListener("keyup",function(){

let value=this.value.toLowerCase();

let cards=document.querySelectorAll(".card");

cards.forEach(card=>{

let name=card.querySelector("h2").innerText.toLowerCase();

let symbol=card.querySelector("h4").innerText.toLowerCase();

if(name.includes(value)||symbol.includes(value)){

card.parentElement.style.display="block";

}else{

card.parentElement.style.display="none";

}

});

});

}

// =========================
// Auto Refresh Every 30 sec
// =========================

setInterval(()=>{

location.reload();

},30000);

// =========================
// Card Animation
// =========================

const observer=new IntersectionObserver((entries)=>{

entries.forEach(entry=>{

if(entry.isIntersecting){

entry.target.style.opacity="1";

entry.target.style.transform="translateY(0)";

}

});

});

document.querySelectorAll(".card").forEach(card=>{

card.style.opacity="0";

card.style.transform="translateY(50px)";

card.style.transition=".6s ease";

observer.observe(card);

});

// =========================
// Navbar Shadow
// =========================

window.addEventListener("scroll",()=>{

const nav=document.querySelector("nav");

if(window.scrollY>20){

nav.style.boxShadow="0 5px 20px rgba(0,212,255,.3)";

}else{

nav.style.boxShadow="none";

}

});

// =========================
// Smooth Scroll
// =========================

document.querySelectorAll('a[href^="#"]').forEach(anchor=>{

anchor.addEventListener("click",function(e){

e.preventDefault();

document.querySelector(this.getAttribute("href")).scrollIntoView({

behavior:"smooth"

});

});

});

// =========================
// Live Time
// =========================

function updateTime(){

const footer=document.querySelector("footer p");

if(footer){

const now=new Date();

footer.innerHTML=
`© 2025 Crypto Tracker | Updated : ${now.toLocaleTimeString()}`;

}

}

updateTime();

setInterval(updateTime,1000);

// =========================
// Hover Effect
// =========================

document.querySelectorAll(".card").forEach(card=>{

card.addEventListener("mouseenter",()=>{

card.style.transform="translateY(-10px) scale(1.02)";

});

card.addEventListener("mouseleave",()=>{

card.style.transform="translateY(0) scale(1)";

});

});

// =========================
// Loading Effect
// =========================

window.onload=()=>{

document.body.style.opacity="1";

}

document.body.style.opacity="0";

document.body.style.transition=".5s";

// =========================
// Console Message
// =========================

console.log("Crypto Tracker Loaded Successfully");
