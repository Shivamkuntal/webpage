const stars = document.querySelectorAll('.star');
const ratingOutput = document.querySelector('.selected-rating');

stars.forEach(star => {
    star.addEventListener('click', function() {
        const value = parseInt(this.getAttribute('data-value'));
        setRating(value);
    });

    star.addEventListener('mouseover', function() {
        const value = parseInt(this.getAttribute('data-value'));
        highlightStars(value);
    });

    star.addEventListener('mouseleave', function() {
        resetStars();
    });
});

function highlightStars(index) {
    stars.forEach((star, i) => {
        if (i < index) {
            star.classList.add('active');
        } else {
            star.classList.remove('active');
        }
    });
}

function resetStars() {
    stars.forEach(star => {
        star.classList.remove('active');
    });
}

function setRating(value) {
    highlightStars(value);
    ratingOutput.textContent = value + ' Stars';
}
function rate(stars) {
    // Here you would typically send the rating to your server using AJAX
    // For simplicity, we'll just show a message here
    document.getElementById('message').innerText = "Thank you for reviewing!";
}
