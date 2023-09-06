function passVisi(input){
    input.type="password";
    if(checkPass.checked){
        input.type="text";
    }
}
function passVisiForCad(){
    passVisi(cadSenha);
    passVisi(cadConfSenha);
}
function passVisiForLog(){
    passVisi(logSenha);
}
function passVisiForNp(){
    passVisi(newPass);
    passVisi(confPass);
}

