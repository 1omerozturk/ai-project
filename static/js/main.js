
const uvideo = document.getElementById("uploaded-video");
const btn=document.getElementById("btnshow");
const shw=document.getElementById("show");
const shw2=document.getElementById("show2");
const video=document.getElementById("video");
const btnup=document.getElementById("btnupload");
const result=document.getElementById("result");
const myform=document.getElementById("myForm");
const load=document.getElementById("idloading");

if (uvideo!=null){

  uvideo.addEventListener("loadeddata",()=>{
    load.classList.add("none");
    shw.classList.remove("hidden");
    shw2.classList.remove("hidden");
  });
}

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