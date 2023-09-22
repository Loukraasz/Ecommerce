function setMargin(img1,img2,img3,img4,img5,img6){
    img1.style.display = "block";
    img2.style.display = "none";
    img3.style.display = "none";
    img4.style.display = "none";
    img5.style.display = "none";
    img6.style.display = "none";

}
function removeMargin(img1,img2,img3,img4,img5,img6){
    img1.style.display = "block";
    img2.style.display = "block";
    img3.style.display = "block";
    img4.style.display = "block";
    img5.style.display = "block";
    img6.style.display = "block";
}
function setAside(aside){
    aside.style.display = "block";
}
function removeAside(aside){
    aside.style.display="none";

}
function denis(){
        setMargin(banner_court,banner_revolution,banner_max,banner_excee,banner_downshifter, banner_soon)
        setAside(info_court)
    }
function remove(){
    removeMargin(banner_court,banner_revolution,banner_max,banner_excee,banner_downshifter, banner_soon)
    removeAside(info_court)
    }

