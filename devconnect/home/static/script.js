// called when a filter for post type is chosen
function filterType() {
    var type = document.getElementById('type');
    console.log(type.value);
    // get filtered posts
    // to add more filters:
    // 1. make a form part for it in the html
    // 2. get its value here
    // 3. add it below to the url, separated by a comma
    // 4. add a query for it in routes.py
    $.ajax({
        url: "/filter/" + type.value + ",",
        type: 'POST',
        data: {
            type: type.value
        },
        dataType: "text",
        success: function (response) {
            console.log('woohoo something happened!')
            console.log(JSON.parse(response).posts)
            showPosts(response);
        }
    });

}

// to show posts to html
function showPosts(postJSON) {
    posts = JSON.parse(postJSON).posts;
    for (let i = 0; i < posts.length; i++) {
        document.getElementById("postType_" + i).innerHTML = convertPostKind(posts[i].kind);
        document.getElementById("postTitle_" + i).innerHTML = posts[i].title;
        document.getElementById("postAuthor_" + i).innerHTML = posts[i].author;
        document.getElementById("postDescrip_" + i).innerHTML = posts[i].descrip;
        console.log("done with: " + i);
    }
}

// convert post kind code to string
function convertPostKind(kind) {
    switch (kind) {
        case "i":
            return "idea"
        case "qa":
            return "q/a"
        case "u":
            return "update"
        default:
            return "something did a big bad"
    }
}