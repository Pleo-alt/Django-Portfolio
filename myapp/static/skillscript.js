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
