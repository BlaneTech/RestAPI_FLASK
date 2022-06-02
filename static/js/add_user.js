let form = document.getElementById("form")
let url = 'http://localhost:8000/groupe4/api/user'
    // let nam = document.getElementById("name")

form.addEventListener('submit', function(e) {
    e.preventDefault()

    let nam = document.getElementById("name").value
    let username = document.getElementById("name").value
    let email = document.getElementById("email").value
    let phone = document.getElementById("phone").value
    let website = document.getElementById("website").value
        // address data
    let street = document.getElementById("street").value
    let suite = document.getElementById("city").value
    let city = document.getElementById("city").value
    let zipcode = document.getElementById("zipcode").value
        // geo data
    let lat = document.getElementById("lat").value
    let lng = document.getElementById("lng").value
        // company data
    let company_name = document.getElementById("company_name").value
    let catchPhrase = document.getElementById("catchPhrase").value
    let bs = document.getElementById("bs").value

    let data = {
        name: nam,
        username: username,
        email: email,
        phone: phone,
        website: website,

        street: street,
        suite: suite,
        city: city,
        zipcode: zipcode,
        lat: lat,
        lng: lng,

        company_name: company_name,
        catchPhrase: catchPhrase,
        bs: bs
    }
    let options = {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            "Content-type": "application/json; charset=UTF-8 ",
            Accept: "application/json"
        }
    }
    fetch(url, options)
        .then(function(response) {
            return response.json()
        })
        // .then(function(data) {
        // console.log(data)
        // })

    window.location.href = '../templates/affiche_user.html'
});


// ----------------Methode à ameliorer------- N'y touche pas please
// async function postFormAddUser({url, formData}){
//     const data = Object.fromEntries(formData.entries());

//     console.log(data)
//     const dataJsonString = JSON.stringify(data);


//     const fetchOptions = {
//         method: "POST",
//         headers:{
//             'Content-Type': 'application/json',
//             Accept: "application/json",
//         },
//         body: dataJsonString,
//     };

//     const response = await fetch(url, fetchOptions);

//     if (!response.ok){
//         const errorMessage = await response.text();
//         throw new Error(errorMessage)
//     }

//     return response.json()
// }

// async function hundleFormSubmit(event){
//     event.preventDefault();

//     const form = event.currentTarget;
//     const url = form.action;

//     try {
//         const formData = new FormData(form);
//         const responseData = await postFormAddUser({url, formData});

//         console.log(responseData)
//     } catch (error) {
//         console.log(error)
//     }
// }

// const form_add = document.getElementById("form_add");
// form_add.addEventListener('submit', hundleFormSubmit)