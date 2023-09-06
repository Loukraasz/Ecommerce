function send(){
    mainForm.addEventListener("submit", false,(e)=>{
    e.preventDefault();
    validate();
    })
}
function validate(){
    passwordValidate();
    confPasswordValidate();
}
function setError(span,input){
    input.style.border = "red 2px solid"; 
    span.style.display = "block";   
}
function removeError(span,input){
    input.style.border = " 3px solid  rgb(252, 189, 255)"; 
    span.style.display = "none";   
}
function passwordValidate(){
    if(newPass.value.length <8){
        setError(spanNp, newPass);
    }
    else if(newPass.value.length >=8){
        removeError(spanNp, newPass);
    }
}
function confPasswordValidate(){
    if(confPass.value != newPass.value){
        setError(spanNpConf, confPass);
    }
    else if (confPass.value == newPass.value){
        removeError(spanNpConf, confPass);
    
    }
}