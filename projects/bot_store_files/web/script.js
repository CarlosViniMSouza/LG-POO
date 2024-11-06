async function sendData() {
    await fetch(
        'http://127.0.0.1:3000/projects/bot_rent_vehicles/bootstrap/index.html', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'Origin',
            "Access-Control-Allow-Credentials": "true"
        },
        body: JSON.stringify({
            "name": document.getElementById("name").value,
            "year": document.getElementById("year").value,
            "daily_value": document.getElementById("dailyvalue").value
        })
    })
        .then(response => {
            if (response.ok) {
                location.href = "./forms/index.html";
            } else {
                throw new Error('Network Response Error!');
            }

            return response.json();
        })
        .then(json => {
            localStorage.setItem('accessToken', JSON.stringify(json.accessToken));
        })
        .catch(error => {
            console.log(error);
        });
}