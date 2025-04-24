function hover(){
    document.getElementById("img").src = "https://grist.org/wp-content/uploads/2015/12/plane.jpg?quality=75&strip=all"
}
function leave(){
    document.getElementById("img").src = "https://images.pexels.com/photos/46148/aircraft-jet-landing-cloud-46148.jpeg"
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