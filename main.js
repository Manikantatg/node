document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData();
    const imageFile = document.getElementById('graphImage').files[0];

    if (imageFile) {
        formData.append('graphImage', imageFile);

        fetch('/analyze', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').innerHTML = `
                <p>Number of Long Paths: ${data.longPaths}</p>
                <p>Number of Short Paths: ${data.shortPaths}</p>
            `;
        })
        .catch(error => console.error('Error:', error));
    }
});
