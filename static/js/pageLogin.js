
function CONNEXION() {
    var COMPTE = [{
        nom: "dabakh",
        passe: "deme",
        profil: "user"
    },
    {
        nom: "weuthie",
        passe: "diop",
        profil: "visiteur"
    },
    {
        nom: "blantech",
        passe: "diaw",
        profil: "admins"
    }]




    var UTILISATEUR = document.getElementById("utilisateur").value;
    var MOTDEPASSE = document.getElementById("motdepasse").value.toString();
    var myError = document.getElementById("erreur")


    if (UTILISATEUR == "" || MOTDEPASSE == "") {
        myError.innerHTML = "Veuillez renseigner tous les champs"
    }
    else {

        for (users of COMPTE) {

            if (UTILISATEUR == users.nom && users == users.passe) {
                window.location.href = "../templates/affiche_user.html";
            }

            else {
                var VALEUR = parseInt(document.getElementById("nombre").value);
                if (isNaN(VALEUR)) { valeur = 0 }

                else {
                    VALEUR++; document.getElementById('nombre').value = VALEUR

                }
                myError.innerHTML = "Nom d'utilistaeur ou mot de passe incorrect"
                myError.style.color = 'red'
            }
        }
    }
        if (VALEUR >= 3) {
            alert('vous avez tenté à plusieurs reprises les mauvaises informations de connexion')
        }


    

}
// CONNEXION()



