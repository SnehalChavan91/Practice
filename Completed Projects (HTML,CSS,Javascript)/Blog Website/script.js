document.addEventListener("DOMContentLoaded", () => {   //sets up an event listener for DOMContentLoaded event, script runs onlu after html content is fully loaded
    const commentForms = document.querySelectorAll(".comment-form");    //selects all elements with class comment-form and store them in NodeList commentForms

    commentForms.forEach(form => {  //iterates over each form in NodeList commentForms
        form.addEventListener("submit" , event => { //adds a submit event listener to each form. When the form is submitted,the callback function runs.
            event.preventDefault(); //Prevents the default behaviour of form submission. Keeps the user on same page after submitting the comment.

            const nameInput = form.querySelector("input").value.trim(); //Fetches the values entered in input and textarea field
            const commentInput = form.querySelector("textarea").value.trim();   //trim() removes the leading and trailing white spaces

            if (nameInput && commentInput) {
                const newComment = document.createElement("li");    //Creates a new <li> element to represent a comment
                newComment.textContent = `${nameInput}: ${commentInput}`;   //sets the textContent to display the comment in the Name: Comment format.

                const commentList = form.parentElement.querySelector(".comment-list");  //selects the ul element(class comment-list) with the same section as the form.
                commentList.appendChild(newComment);    //appends the newly created <li> comment to the comment-list.

                form.querySelector("input").value = ""; //clears the input and textarea fields in the form.
                form.querySelector("textarea").value = "";  //prepares the form for a new submission.
            } else {
                alert("Please fill in both the name and the comment fields.");
            }
        });
    });
});