
function CONNEXION(){
    var COMPTE ={
        nom: "dabakh",
        passe:"deme",

        nom: "weuthie",
        passe:"diop",

        nom: "blantech",
        passe: "diaw"}
    

   console.log(COMPTE)
    
    var UTILISATEUR = document.getElementById("utilisateur").value.toString().trim();
    var MOTDEPASSE = document.getElementById("motdepasse").value.toString().trim();
    var myError = document.getElementById("erreur")


    if (UTILISATEUR=="" || MOTDEPASSE==""){
        myError.innerHTML= "Veuillez renseigner tous les champs"
    }
    else{
        if ((UTILISATEUR==COMPTE.nom && MOTDEPASSE == COMPTE.passe) || (UTILISATEUR==COMPTE2.nom && MOTDEPASSE == COMPTE2.passe) || (UTILISATEUR==COMPTE3.nom && MOTDEPASSE == COMPTE3.passe)){
             window.location.href="../templates/affiche_user.html";
            // window.location.href ="http://127.0.0.1:5000/pagePrincipal"
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



