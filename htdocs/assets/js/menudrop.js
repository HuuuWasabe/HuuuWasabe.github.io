// menu drop js

document.addEventListener("DOMContentLoaded", () => {
    const toggles = document.querySelectorAll(".menu-drop");

    toggles.forEach(toggle => {
        toggle.addEventListener("click", (e) => {
        e.preventDefault(); // prevent link from navigating

        const dropdown = toggle.nextElementSibling;

        // Close other open dropdowns for cleaner transition
        document.querySelectorAll(".menu-drop-show").forEach(openMenu => {
            if (openMenu !== dropdown) openMenu.classList.remove("show");
        });

        // Toggle the dropdown when clicked
        dropdown.classList.toggle("show");
    });
    });

    // Close dropdown when clicked outsise
    document.addEventListener("click", (e) => {
        if (!e.target.closest("li")) {
            document.querySelectorAll(".menu-drop-show").forEach(openMenu => {
                openMenu.classList.remove("show");
            });
        }
    })
});