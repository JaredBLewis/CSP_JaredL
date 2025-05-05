function show(){
    if(document.getElementById("hidden").style.display === "block"){
        document.getElementById("hidden").style.display = "none"
        document.getElementById("button").innerHTML = "Show More"
    }else{
    document.getElementById("hidden").style.display = "block"
    document.getElementById("button").innerHTML = "Show Less"}
}