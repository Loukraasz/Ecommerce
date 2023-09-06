const emailRegex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
function send(){
    formRecPassword.addEventListener("submit",false, (e)=>{
        e.preventDefault();
        emailValidate();  
        })
    }
function setError(span,input){
    input.style.border = "red 2px solid"; 
    span.style.display = "block";   
}
function removeError(span,input){
    input.style.border = " 3px solid  rgb(252, 189, 255)"; 
    span.style.display = "none";   
}
function okEmail(){
    spanREmailExists.style.display = "none";  
}
function emailValidate(){
    if(!emailRegex.test(rEmail.value)){
        setError(spanREmail, rEmail);
    }
    else if(emailRegex.test(rEmail.value)){
        removeError(spanREmail,rEmail);
        removeError(spanREmailExists,rEmail);
        }
}