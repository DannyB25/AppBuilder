document.addEventListener('DOMContentLoaded', function() {
    // Get the images
    var image1 = document.getElementById('image1');
    var image2 = document.getElementById('image2');
    var image3 = document.getElementById('image3');
    var image4 = document.getElementById('image4');

    // Set the interval time (in milliseconds)
    const intervalTime = 1000; // 1 seconds

    // Function to switch images on the left
    function switchImages() {
        if (image1.style.opacity === '0') {
            image1.style.opacity = '1';
            image2.style.opacity = '0';
        }
        else {
            image1.style.opacity = '0';
            image2.style.opacity = '1';
        }
    }

    const intervalTime2 = 1000; // 1 seconds
    // Function to switch images on the right
    function switchImages2() {
        if (image3.style.opacity === '0') {
            image3.style.opacity = '1';
            image4.style.opacity = '0';
        }
        else {
            image3.style.opacity = '0';
            image4.style.opacity = '1';
        }
    }

    // Set interval to switch images
    setInterval(switchImages, intervalTime);

    //Set interval to switch images
    setInterval(switchImages2, intervalTime2);

    const form = document.getElementById('edit-form');
    form.addEventListener('submit', function(event) {
        const saveButton = document.getElementById('save-button');
        const deleteButton = document.getElementById('delete-button');

        // Check which button was clicked
        if (event.submitter === saveButton) {
            const confirmSave = confirm("Are you sure you want to save changes?");
            if (!confirmSave) {
                event.preventDefault(); // Prevent form submission if the user cancels
            }
        } else if (event.submitter === deleteButton) {
            const confirmDelete = confirm("Are you sure you want to delete this item? This action cannot be undone.");
            if (!confirmDelete) {
                event.preventDefault(); // Prevent form submission if the user cancels
            }
        }
    });
});

