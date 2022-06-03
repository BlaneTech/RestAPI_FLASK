let ligne = "";
const listUser = document.querySelector(".listUsers");
fetch("http://localhost:8000/groupe4/api/users")
  .then((rep) => rep.json())
  .then((rep) => {
    rep.forEach((user) => {
      ligne += `
    <tr class="tr">      
        <td class="radio"><input type="radio" name="select" ></td>
        <td class="td id">${user.id}</td>
        <td class="td">${user.name}</td>
        <td class="td" >${user.email}</td>
        <td class="td" >${user.phone}</td>

<td class="actions"><input type="button" class="update" value="update"> <input  type="button" class="delete" value="delete"> <input type="button"  class="voir_plus" value="voir plus"> </td>

        </tr>`;
    });
    listUser.innerHTML = ligne;
    let c = document.querySelector("tbody");
    c.addEventListener("click", (e) => {
      let btn = e.target;
      if (btn.type == "radio") {
        var radio = document.getElementsByName("select");
        for (var i = 0; i < radio.length; i++) {
          radio[i].addEventListener("click", (e) => {
            var el = document.querySelector(".tr");
            g = e.target;
            g.parentElement.parentElement;
            var lesfils = g.parentElement.parentElement;
            var listdesfils = lesfils.children;

            inputs = document.querySelectorAll(".myInput");
            for (let element of inputs) {
              element.parentNode.innerText = element.value;
              element.remove();
            }
            for (let i = 2; i < listdesfils.length - 1; i++) {
              var input2 = document.createElement("input");
              input2.classList.add("myInput");
              input2.setAttribute("type", "text");
              input2.value = listdesfils[i].innerText;
              listdesfils[i].innerText = "";
              listdesfils[i].append(input2);
            }
          });
        }
    }else{
        
    if(btn.getAttribute("class")==="td"){
            btn.addEventListener('click',(e)=>{
                var champ=e.target
                var input = document.createElement('input')
                input.setAttribute("type","text")
                if(champ.innerText){
                    input.value=champ.innerText
                    champ.innerText=""
                    champ.append(input)
                    input.addEventListener('blur',()=>{
                    champ.innerText=input.value
                    input.remove() 
                    })
                }
                
            }) 
        }
        
    }
    // console.log(deleteBtn.length)
    // ############# Voir plus ######################
    let voirPlusBtn = document.querySelectorAll(".voir_plus");
    console.log(voirPlusBtn.length);
    voirPlusBtn.forEach((btn) => {
      btn.addEventListener("click", (e) => {
        const id = parseInt(
          e.target.parentNode.parentNode.children[1].innerText
        );
        localStorage.setItem("id", `${id}`);
        window.location.href = "../templates/user.html";
      });
    });
  });

 });
// #################UPDATE##################

var id = parseInt(localStorage.getItem("id"));
const nom = document.querySelector("#name");
const username = document.querySelector("#username");
const email = document.querySelector("#email");
const phone = document.querySelector("#phone");
const website = document.querySelector("#website");
const street = document.querySelector("#street");
const suite = document.querySelector("#suite");
const city = document.querySelector("#city");
const zipcode = document.querySelector("#zipcode");
const lat = document.querySelector("#lat");
const lng = document.querySelector("#lng");
const NAME = document.querySelector("#company_name");
const catchPhrase = document.querySelector("#catchPhrase");
const bs = document.querySelector("#bs");
let modifieBtn = document.querySelector("#submit");

function popupUpdate() {
  let updateBtn = document.querySelectorAll(".update");
  let popup = document.querySelector(".cadre");
  let closeBtn = document.querySelector("em");
  let containtPopupStyle = document.getElementById("containtPopup");

  for (btn of updateBtn) {
    btn.addEventListener("click", (e) => {
      popup.style.display = "block";
      containtPopupStyle.classList.add("containtPopup");
      console.log(popup.style.display);

      ////deme
      const id = parseInt(e.target.parentNode.parentNode.children[1].innerText);
      fetch(`http://localhost:8000/groupe4/api/users/${id}`)
        .then((rep) => rep.json())
        .then((rep) => {
          nom.value = rep.name;
          username.value = rep.username;
          email.value = rep.email;
          website.value = rep.website;
          phone.value = rep.phone;
          street.value = rep.address.street;
          city.value = rep.address.city;
          suite.value = rep.address.suite;
          zipcode.value = rep.address.zipcode;
          zipcode.value = rep.address.zipcode;
          lat.value = parseFloat(rep.address.geo.lat);
          lng.value = parseFloat(rep.address.geo.lng);
          NAME.value = rep.company.name;
          catchPhrase.value = rep.company.catchPhrase;
          bs.value = rep.company.bs;
          modifieBtn.addEventListener("click", (e) => {
            e.preventDefault();
            var data = {
              name: nom.value,
              username: username.value,
              email: email.value,
              phone: phone.value,
              website: website.value,
              street: street.value,
              suite: suite.value,
              city: city.value,
              zipcode: zipcode.value,
              lat: lat.value,
              lng: lng.value,
              company_name: NAME.value,
              catchphrase: catchPhrase.value,
              bs: bs.value,
            };

            fetch(`http://localhost:8000/groupe4/api/users/${id}`, {
              method: "PATCH",
              headers: {
                "Content-Type": "application/json",
              },
              body: JSON.stringify(data),
            });
            // console.log(data);
            // popup.style.display = "none";
            // containtPopupStyle.classList.remove("containtPopup");

            window.location.reload()
          });
        });
      //
    });
  }
  closeBtn.addEventListener("click", () => {
    popup.style.display = "none";
    containtPopupStyle.classList.remove("containtPopup");
  });
}
