let ligne=""
const listUser = document.querySelector(".listUsers")
fetch('http://localhost:8000/groupe4/api/users')
.then(rep=>rep.json())
.then(rep=>{ 
    rep.forEach(user=> {
    ligne+=`
    <tr class="tr">      
        <td class="radio"><input type="radio" name="select" ></td>
        <td>${user.id}</td>
        <td class="td">${user.name}</td>
        <td class="td" >${user.email}</td>
        <td class="td" >${user.phone}</td>

<td ><input type="button" class="update" value="update"> <input  type="button" class="delete" value="delete"> <input type="button"  class="voir_plus" value="voir plus"> </td>

        </tr> 
        `
});
 listUser.innerHTML=ligne;   
let c=document.querySelector("tbody")
c.addEventListener("click",(e)=>{
    let btn=e.target
    console.log(btn.getAttribute("class"))
    if(btn.type == "radio"){ 
        var radio = document.getElementsByName("select");
        for( var i=0;i<radio.length;i++){
            radio[i].addEventListener('click',(e)=>{
            var el = document.querySelector(".tr")
            g=e.target
            g.parentElement.parentElement
            var lesfils=g.parentElement.parentElement
            var listdesfils = lesfils.children

            inputs = document.querySelectorAll('.myInput')
            for(let element of inputs){
                element.parentNode.innerText = element.value
                element.remove()
            }
            for(let i=2;i<listdesfils.length-1;i++){ 
                var input2 = document.createElement('input')
                input2.classList.add("myInput")
                input2.setAttribute("type","text")
                input2.value=listdesfils[i].innerText
                listdesfils[i].innerText=""
                listdesfils[i].append(input2)        
        }
            })
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
    popupUpdate()

})
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
let voirPlusBtn = document.querySelectorAll('.voir_plus')
console.log(voirPlusBtn.length)
voirPlusBtn.forEach(btn => {
    btn.addEventListener('click',(e)=>{
        const id = parseInt(e.target.parentNode.parentNode.children[1].innerText);
        localStorage.setItem('id',`${id}`)
        window.location.href="../templates/user.html"
    })

})
  
})

// });
// #################UPDATE##################
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
