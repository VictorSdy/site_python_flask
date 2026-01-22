function loadPage(url) {
    fetch(url)

        .then(response => response.text())
        .then(html => {
            document.getElementById("content-box").innerHTML = html;
        })
        .catch(() => {
            document.getElementById("content-box").innerHTML =
                "<p>Erreur de chargement</p>";
        });
}
