
const uvideo = document.getElementById("uploaded-video");
const btn=document.getElementById("btnshow");
const shw=document.getElementById("show");
const shw2=document.getElementById("show2");
const video=document.getElementById("video");
const btnup=document.getElementById("btnupload");
const result=document.getElementById("result");
const myform=document.getElementById("myForm");
const load=document.getElementById("idloading");

// Başlık Animasyounu
document.addEventListener("DOMContentLoaded", function() {
  const baslik = document.getElementById("animasyon-baslik");
  const metin = baslik.innerHTML;
  baslik.innerHTML = "";

  for (let i = 0; i < metin.length; i++) {
    setTimeout(function() {
      baslik.innerHTML += metin[i];
      if (i === metin.length - 1) {
        baslik.style.animation = "yazim-animasyon 1s steps(40, end) forwards";
        setTimeout(function() {
          baslik.style.borderRight = "none";
        }, 1000);
       }
    }, i * 110); 
  }
});



// Video seçilmemiş ise

if (uvideo!=null){

  uvideo.addEventListener("loadeddata",()=>{
    load.classList.add("none");
    shw.classList.remove("hidden");
    shw2.classList.remove("hidden");
  });
}
video.addEventListener("change",()=>
{
  btnup.classList.remove("hidden");
}
  );



btnup.addEventListener("click",function (event) {
  
load.classList.remove("hidden");
});




btn.addEventListener("click",()=>{
  result.classList.remove("hidden");
});
  if(uvideo!=null){
    
  uvideo.addEventListener("click", function () {
    if (uvideo.paused) {
      uvideo.play();
    } else {
      uvideo.pause();
    }
  });
}