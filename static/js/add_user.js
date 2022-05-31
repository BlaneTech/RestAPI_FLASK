async function postFormAddUser({url, formData}){
    const data = Object.fromEntries(formData.entries());

    console.log(data)
    const dataJsonString = JSON.stringify(data);


    const fetchOptions = {
        method: "POST",
        headers:{
            'Content-Type': 'application/json',
            Accept: "application/json",
        },
        body: dataJsonString,
    };

    const response = await fetch(url, fetchOptions);

    if (!response.ok){
        const errorMessage = await response.text();
        throw new Error(errorMessage)
    }

    return response.json()
}

async function hundleFormSubmit(event){
    event.preventDefault();

    const form = event.currentTarget;
    const url = form.action;

    try {
        const formData = new FormData(form);
        const responseData = await postFormAddUser({url, formData});

        console.log(responseData)
    } catch (error) {
        console.log(error)
    }
}

const form_add = document.getElementById("form_add");
form_add.addEventListener('submit', hundleFormSubmit)