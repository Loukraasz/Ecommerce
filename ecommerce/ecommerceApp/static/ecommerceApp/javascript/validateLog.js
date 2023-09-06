function setError(span,input){
    input.style.border = "red 2px solid"; 
    span.style.display = "block";   
}
function removeError(span,input){
    input.style.border = " 3px solid  rgb(252, 189, 255)"; 
    span.style.display = "none";   
}
function okPass(){
    spanLogPassIn.style.display = "none";  
}