var id =parseInt(localStorage.getItem('id'))
const nom =document.querySelector(".name")
const username =document.querySelector(".username")
const email =document.querySelector(".email")
const phone =document.querySelector(".phone")
const website =document.querySelector(".website")
const street =document.querySelector(".street")
const suite =document.querySelector(".suite")
const city =document.querySelector(".city")
const zipcode =document.querySelector(".zipcode")
const lat =document.querySelector(".lat")
const lng =document.querySelector(".lng")
const NAME =document.querySelector(".NAME")
const CATCHPHRASE =document.querySelector(".CATCHPHRASE")
const bs =document.querySelector(".bs")

fetch(`http://localhost:8000/groupe4/api/users/${id}`)
        .then(rep=>rep.json())
        .then(rep=>{
            console.log(rep)
            nom.innerText = rep.name
            username.innerText= rep.username
            email.innerText= rep.email
            website.innerText= rep.website
            phone.innerText= rep.phone
            street.innerText= rep.address.street
            city.innerText= rep.address.city
            suite.innerText= rep.address.suite
            zipcode.innerText= rep.address.zipcode
            zipcode.innerText= rep.address.zipcode
            lat.innerText = rep.address.geo.lat
            lng.innerText = rep.address.geo.lng
            NAME.innerText= rep.company.name
            CATCHPHRASE.innerText = rep.company.catchPhrase
            bs.innerText = rep.company.bs
        })