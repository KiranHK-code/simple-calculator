let btn=document.querySelectorAll("button");
let box=document.querySelector(".click");

btn.forEach((button)=>{
    button.addEventListener("click",()=>
{
    box.innerHTML="button"
})
}) 

