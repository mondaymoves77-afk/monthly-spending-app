const form=document.getElementById("form"),loginCard=document.getElementById("loginCard"),resultCard=document.getElementById("resultCard"),btn=document.getElementById("loginBtn"),error=document.getElementById("error");
form.addEventListener("submit",async e=>{
 e.preventDefault(); error.textContent=""; btn.disabled=true; btn.textContent="جارٍ التحقق...";
 try{
  const r=await fetch("/api/login",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({name:document.getElementById("name").value,password:document.getElementById("password").value})});
  const d=await r.json(); if(!r.ok) throw new Error(d.message);
  document.getElementById("userName").textContent=d.name;
  document.getElementById("avatar").textContent=d.name.charAt(0);
  document.getElementById("amount").textContent=Number(d.amount).toLocaleString("ar-EG");
  document.getElementById("message").textContent=d.message;
  loginCard.classList.add("hidden");resultCard.classList.remove("hidden");
 }catch(x){error.textContent=x.message||"تعذر الاتصال بالسيرفر."}
 finally{btn.disabled=false;btn.innerHTML='دخول إلى حسابي <b>←</b>'}
});
document.getElementById("logout").addEventListener("click",()=>{resultCard.classList.add("hidden");loginCard.classList.remove("hidden");form.reset();document.getElementById("name").focus()});
