
function CONNEXION(){
    var COMPTE ={
        nom: "dabakh",
        passe:"deme",
    }
    
    var UTILISATEUR = document.getElementById("utilisateur").value.toString().trim();
    var MOTDEPASSE = document.getElementById("motdepasse").value.toString().trim();
    var myError = document.getElementById("erreur")


    if (UTILISATEUR=="" || MOTDEPASSE==""){
        myError.innerHTML= "Veuillez renseigner tous les champs"
    }
    else{
        if (UTILISATEUR==COMPTE.nom && MOTDEPASSE == COMPTE.passe){
            window.location.href="../connexion/auth.html";
        }
        else{
            var VALEUR = parseInt(document.getElementById("nombre").value);
                if(isNaN(VALEUR)){valeur = 0} 

                    else{
                        VALEUR++; document.getElementById('nombre').value=VALEUR

                    }
                myError.innerHTML = "Nom d'utilistaeur ou mot de passe incorrect"
                myError.style.color = 'red'

            if (VALEUR >= 3){
                alert('vous avez tenté à plusieurs reprises les mauvaises informations de connexion')
            }
        }
    }

}

