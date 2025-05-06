function show(){
    if(document.getElementById("hidden").style.display === "flex"){
        document.getElementById("hidden").style.display = "none"
        document.getElementById("button").innerHTML = "Show More"
    }else{
    document.getElementById("hidden").style.display = "flex"
    document.getElementById("button").innerHTML = "Show Less"}
}
function change() {
    const img = document.getElementById("img1");
    img.src = "https://i.etsystatic.com/23026333/r/il/81f397/5173472100/il_fullxfull.5173472100_iir3.jpg";
}
function resetImage() {
    const img = document.getElementById("img1");
    img.src = "https://images.squarespace-cdn.com/content/v1/536d357ee4b0b850609e0eb2/1549656433531-0TYFQ99EKNW4AW334LCN/IMG_1314.jpg";
}