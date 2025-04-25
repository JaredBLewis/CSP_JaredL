function change() {
    const img = document.getElementById("img");
    img.src = "https://static.vecteezy.com/system/resources/thumbnails/047/269/681/small_2x/thumb-up-emoji-isolated-in-transparent-background-png.png";
    document.getElementById("imgsrc").innerHTML = "Image From: Vectreezy";
}

function ResetImage() {
    const img = document.getElementById("img");
    img.src = "https://media.cnn.com/api/v1/images/stellar/prod/210910234902-01-vaccine-protest-ca-0829.jpg?q=w_3000,h_2000,x_0,y_0,c_fill";
    document.getElementById("imgsrc").innerHTML = "Image From: CNN";
}

function view(){
    if(document.getElementById("paragraph").style.display === "block"){
        document.getElementById("paragraph").style.display = "none"
        document.getElementById("btn").innerHTML = "Show More"
    }else{
    document.getElementById("paragraph").style.display = "block"
    document.getElementById("btn").innerHTML = "Show Less"
    }
}
function scrollToBottom() {
    window.scrollTo({
        top: document.body.scrollHeight,
        behavior: "smooth"
    });
}