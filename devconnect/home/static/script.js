// called when a filter for post type is chosen
function filterType() {
    var type = document.getElementById('type');
    var author = document.getElementById('author');
    console.log(type.value);
    console.log(author.value);
    // get filtered posts
    $.ajax({
        url: "/filter/" + type.value + "," + author.value,
        type: 'POST',
        data: {
            type: type.value,
            author: author.value
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
    posts = JSON.parse(postJSON).posts
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