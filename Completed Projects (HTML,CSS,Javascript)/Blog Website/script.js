document.addEventListener("DOMContentLoaded", () => {
    const commentForms = document.querySelectorAll(".comment-form");

    commentForms.forEach(form => {
        form.addEventListener("submit" , event => {
            event.preventDefault();

            const nameInput = form.querySelector("input").value.trim();
            const commentInput = form.querySelector("textarea").value.trim();

            if (nameInput && commentInput) {
                const newComment = document.createElement("li");
                newComment.textContent = `${nameInput}: ${commentInput}`;

                const commentList = form.parentElement.querySelector(".comment-list");
                commentList.appendChild(newComment);

                form.querySelector("input").value = "";
                form.querySelector("textarea").value = "";
            } else {
                alert("Please fill in both the name and the comment fields.");
            }
        });
    });
});