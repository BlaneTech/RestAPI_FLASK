let ligne = "";
const listUser = document.querySelector(".listUsers");
fetch("http://localhost:8000/groupe4/api/users")
  .then((rep) => rep.json())
  // console.log(rep)
  .then((rep) => {
    rep.forEach((user) => {
      ligne += `
    <tr class="tr">      
        <td class="radio"><input type="radio" name="select" ></td>
        <td class="td id">${user.id}</td>
        <td class="td">${user.name}</td>
        <td class="td" >${user.email}</td>
        <td class="td" >${user.phone}</td>
        <td >
            <input type="button" class="update" value="update"> 
            <input  type="button" class="delete" value="delete"> 
            <input type="button"  class="voir_plus" value="voir plus"> 
        </td>
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
            // while(el===el.nextSibling){
            // if(el.tagName==="TR"){
            //    el.classList.remove("selected")
            // }
            // }
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
      } else {
        btn.addEventListener("click", (e) => {
          var input = document.createElement("input");
          input.setAttribute("type", "text");
          input.value = e.target.innerText;
          e.target.innerText = "";
          e.target.append(input);
          input.addEventListener("blur", () => {
            e.target.innerText = input.value;
            input.remove();
          });
        });
      }
    });
    // "####################update##############################"
    popupUpdate();
  });
// ########################delete########################
var table = document.querySelector('tbody')
let ligneSupp= document.querySelectorAll('tr')
let deleteBtn = document.querySelectorAll('.delete')
for (i=0; i<deleteBtn.length; i++){
    deleteBtn[i].addEventListener('click',(e)=>{
        console.log('delete')
        var deleteId = parseInt(e.target.parentNode.parentNode.children[1].innerText)
        fetch(`http://localhost:8000/groupe4/api/users/${deleteId}`,{
            method:'DELETE',
            headers: {
              'Content-Type':'application/json',
            }
            })
    })

}
// console.log(deleteBtn.length)
// ############# Voir plus ######################
let voirPlusBtn = document.querySelectorAll(".voir_plus");
console.log(deleteBtn.length);
voirPlusBtn.forEach((btn) => {
  btn.addEventListener("click", (e) => {
    const id = parseInt(e.target.parentNode.parentNode.children[1].innerText);

    console.log(id);
    console.log("voir plus");
    fetch("http://localhost:8000/groupe4/api/users/1")
      .then((rep) => rep.json())
      .then((rep) => {
        rep.forEach((user) => {
          console.log(user);
        });
      });
  });
});

// });

function popupUpdate() {
  let updateBtn = document.querySelectorAll(".update");
  let popup = document.querySelector(".cadre");
  let closeBtn = document.querySelector('em')
  for (btn of updateBtn) {
    btn.addEventListener("click", (e) => {
      popup.style.display = "block";
      console.log(popup.style.display);
    });
  }
  closeBtn.addEventListener('click', ()=>{
    popup.style.display = "none";

  })
}

// window.addEventListener("scroll",()=>{
// console.log(innerHeight+scrollY, document.documentElement.scrollHeight)
// if(innerHeight+scrollY+10 >= document.documentElement.scrollHeight){
// console.log("bonjour")
// fetch('http://localhost:8000/groupe4/api/users')
// .then(rep=>rep.json())
// .then(rep=>{rep.forEach(user=> {
// ligne+=`
// <tr class="tr">
// <td> <input type="radio" name="select" ></td>
// <td class="td">${user.name}</td>
// <td class="td" >${user.email}</td>
// <td class="td" >${user.phone}</td>
// <td ><input type="button" value="update"> <input type="button" value="delete"> <input type="button" value="voir plus"> </td>
// </tr>
// `
// });
//  listUser.innerHTML=ligne;
// })
// }
// })

// var tr = document.getElementsByClassName('tr')
// console.log(tr)
// for (var i = 0; i< tr.length; i++){
// var col = tr[i]
// console.log(col)
// var colore = function(){
// this.classList.toggle('red')
// }
// package.addEventListener('click', colore)
// }

var tabTr = document.querySelector("tbody");
// var tab = tabTr[0].querySelector('tr')
console.log(tabTr);
// console.log(tab)
for (let tr = 0; tr < tabTr.length; tr++) {
  tr.addEventListener("click", function () {
    this.classList.toggle("gris");
    console.log(tr);
  });
}
