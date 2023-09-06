/*
funcao send(), responsavel por validar e impedir o envio de formulario caso os requisitos nao sejam atingidos
*/
const emailRegex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
function send(){
    mainForm.addEventListener("submit", false,(e)=>{
    e.preventDefault();
    nameValidate();
    emailValidate();
    passwordValidate();
    confPasswordValidate();
    okName();
    
    })
}

/*
funcao setError() , okEmail() removeError(), responsaveis por remover ou acionar mensagens de erros do formulario
*/
function setError(span,input){
    input.style.border = "red 2px solid"; 
    span.style.display = "block";   
}
function removeError(span,input){
    input.style.border = " 3px solid  rgb(252, 189, 255)"; 
    span.style.display = "none";   
}
function okEmail(){
    spanCadEmailExists.style.display = "none";  
}
function okName(){
    spanCadNomeExists.style.display = "none";
    spanCadNomeNot.style.display = "none";
}

/*
funcao nameValidate(), emailValidate(), passwordValidate() e confPasswordValidate(), sao responsaveis das validacoes dos campos do formulario
*/
function nameValidate(){
    if(cadNome.value.length <3 || cadNome.value == ""){
        setError(spanCadNome, cadNome);
    }
    else if (cadNome.value.length > 3){
        removeError(spanCadNome,cadNome)
        removeError(spanCadNomeExists,cadNome)
    }
}
function emailValidate(){
    if(!emailRegex.test(cadEmail.value)){
        setError(spanCadEmail, cadEmail);
    }
    else if(emailRegex.test(cadEmail.value)){
        removeError(spanCadEmail,cadEmail);
        removeError(spanCadEmailExists,cadEmail);
        }
}
function passwordValidate(){
    if(cadSenha.value.length <8){
        setError(spanCadSenha, cadSenha);
    }
    else if(cadSenha.value.length >=8){
        removeError(spanCadSenha, cadSenha);
    }
}
function confPasswordValidate(){
    if(cadConfSenha.value != cadSenha.value){
        setError(spanCadConfSenha, cadConfSenha);
    }
    else if (cadConfSenha.value == cadSenha.value){
        removeError(spanCadConfSenha, cadConfSenha);
    
    }
}


    
   

