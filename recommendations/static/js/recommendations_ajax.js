document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById('recommendation-form');
    const submitButton = document.querySelector('button[type="submit"]');
    form.addEventListener('submit', function(e) {
        e.preventDefault();

    submitButton.textContent = "Roll again!";

        const formData = new FormData(form);
        const favorites = formData.getAll('favorites');

        fetch('/api/recommendations/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: JSON.stringify({ 'favorites': favorites })
        })
        .then(response => response.json())
        .then(data => {
            const outputDiv = document.getElementById('recommendations-output');
            outputDiv.innerHTML = '';  // Clear previous results

            // Checking if 'recommendation' key exists in the response and has content
            if (data.recommendation && data.recommendation.name) {
                // Dynamically creating HTML to display the recommendation details
                const restaurantDiv = document.createElement('div');
                restaurantDiv.innerHTML = `
                    <h3>${data.recommendation.name}</h3>
                    <p>${data.recommendation.description}</p>
                    <p><strong>Address:</strong> ${data.recommendation.address}</p>
                    <p><strong>Phone:</strong> ${data.recommendation.phone}</p>
                    <a href="${data.recommendation.website}" target="_blank">Visit Website</a>
                `;
                outputDiv.appendChild(restaurantDiv);
            } else {
                outputDiv.textContent = 'No recommendations found.';
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
            });
        });

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
