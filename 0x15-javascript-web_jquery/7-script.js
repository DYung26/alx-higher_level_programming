fetch('https://swapi-api.alx-tools.com/api/people/5/?format=json')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json(); // Parse the response as JSON
    })
    .then(data => {
        const extractedName = data.name;
        $('#character').text(`${extractedName}`);
    })
