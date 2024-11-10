// Function to handle the animation of skill bars when section is in view
document.addEventListener("DOMContentLoaded", function () {
    const skillBars = document.querySelectorAll('.skills__percentage');

    // Function to animate bars based on data-percentage
    function animateSkills() {
        skillBars.forEach(bar => {
            const percentage = bar.getAttribute('data-percentage');
            bar.style.width = `${percentage}%`;  // Set width based on data-percentage
        });
    }

    // Checking if the section is in view
    function checkSkillsInView() {
        const skillsSection = document.getElementById('skills');
        const sectionTop = skillsSection.getBoundingClientRect().top;
        const sectionBottom = skillsSection.getBoundingClientRect().bottom;

        if (sectionTop < window.innerHeight && sectionBottom > 0) {
            animateSkills();
            window.removeEventListener('scroll', checkSkillsInView);  // Remove listener after animation
        }
    }

    window.addEventListener('scroll', checkSkillsInView);
    checkSkillsInView();  // Initial check in case the section is already in view
});

 // Get all navigation links
const navLinks = document.querySelectorAll('.nav__link');

// Function to handle click events
navLinks.forEach(link => {
    link.addEventListener('click', function() {
        // Remove active class from all links
        navLinks.forEach(link => link.classList.remove('active'));
        // Add active class to the clicked link
        this.classList.add('active');
    });
});

// Set up IntersectionObserver
const sections = document.querySelectorAll('section');
const options = {
    root: null, // Use the viewport as the root
    threshold: 0.5 // Trigger when 50% of the section is in view
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        const id = entry.target.id;
        const navLink = document.querySelector(`nav ul li a[href="#${id}"]`);

          // Check if the section is the Contact section
          if (id === "contact") {
            // Set a higher threshold (1) for the Contact section
            const contactOptions = {
                root: null,
                threshold: .6 // Only trigger when 100% of the Contact section is visible
            };
            const contactObserver = new IntersectionObserver((contactEntries) => {
                contactEntries.forEach(contactEntry => {
                    const contactNavLink = document.querySelector(`nav ul li a[href="#contact"]`);
                    if (contactEntry.isIntersecting) {
                        navLinks.forEach(link => link.classList.remove('active'));
                        contactNavLink.classList.add('active');
                    }
                });
            }, contactOptions);
            contactObserver.observe(entry.target);
        } else {
            // Default behavior for other sections
            if (entry.isIntersecting) {
                navLinks.forEach(link => link.classList.remove('active'));
                navLink.classList.add('active');
            }
        }
    });
}, options);

// Observe each section
sections.forEach(section => {
    observer.observe(section);
});
document.addEventListener('DOMContentLoaded', function () {
    const modal = document.getElementById('modal');
    const closeModal = document.querySelector('.modal-close');
    const modalCategoryItems = document.getElementById('modal-category-items');
    const openModalLinks = document.querySelectorAll('.open-modal');

    openModalLinks.forEach(link => {
        link.addEventListener('click', function (event) {
            const projectId = event.currentTarget.getAttribute('data-project-id');
            
            // Fetch categories related to the clicked project
            fetch(`/get-categories/${projectId}/`)
                .then(response => response.json())
                .then(data => {
                    modalCategoryItems.innerHTML = '';  // Clear existing categories

                    if (data.length > 0) {
                        data.forEach(category => {
                            const categoryElement = document.createElement('div');
                            categoryElement.classList.add('category-item');
                            categoryElement.innerHTML = `
                                <img src="${category.image}" alt="${category.name}">
                                <h4>${category.name}</h4>
                                <p>${category.description}</p>
                                <a href="${category.github_url}" target="_blank">View on GitHub</a>
                            `;
                            modalCategoryItems.appendChild(categoryElement);
                        });
                    } else {
                        modalCategoryItems.innerHTML = '<p>No categories available.</p>';
                    }

                    modal.style.display = 'block';  // Show the modal
                })
                .catch(error => {
                    console.error('Error fetching categories:', error);
                    modalCategoryItems.innerHTML = '<p>Error loading categories.</p>';
                });
        });
    });

    // Close the modal
    closeModal.addEventListener('click', function () {
        modal.style.display = 'none';
    });

    // Close the modal if the user clicks outside of it
    window.addEventListener('click', function (event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
});



document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');
    const successMessage = document.getElementById('contactSuccessMessage');

    contactForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission behavior

        const formData = new FormData(contactForm);

        fetch(contactForm.action, {
            method: 'POST',
            body: formData
        })
        .then(response => response.json()) // Assume response is JSON with success status
        .then(data => {
            if (data.success) {
                successMessage.style.display = 'block'; // Show success message
                contactForm.reset(); // Optionally reset the form
            } else {
                alert('There was an error sending your message.');
            }
        })
        .catch(error => {
            alert('There was an error sending your message.');
        });
    });
});

