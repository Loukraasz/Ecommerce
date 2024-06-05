function setMargin(img1,img2,img3,img4){
    img1.style.display = "block";
    img2.style.display = "none";
    img3.style.display = "none";
    img4.style.display = "none";
    


}
function removeMargin(img1,img2,img3,img4){
    img1.style.display = "block";
    img2.style.display = "block";
    img3.style.display = "block";
    img4.style.display = "block";
    
}
function setAside(aside){
    aside.style.display = "block";
}
function removeAside(aside){
    aside.style.display="none";

}
function set(img1,img2,img3,img4,info){
        setMargin(img1,img2,img3,img4)
        setAside(info)
    }
function remove(info){
    removeMargin(banner_court,banner_revolution,banner_excee,banner_downshifter)
    removeAside(info)
    }
function onlyRight(img1,img2,img3,img4,info){
    set(img1,img2,img3,img4,info)
}

