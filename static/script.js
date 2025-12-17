const BASE_URL = "http://127.0.0.1:8000";

async function getSongRecommendations() {
    const song = document.getElementById("songInput").value;
    const res = document.getElementById("results");

    res.innerHTML = "Loading...";

    const response = await fetch(`${BASE_URL}/recommend?song=${song}`);
    const data = await response.json();

    let html = "<h3>Recommended Songs</h3><ul>";
    data.recommendations.forEach(r => {
        html += `<li>${r.song} — ${r.artist}</li>`;
    });
    html += "</ul>";

    res.innerHTML = html;
}

async function getMoodRecommendations() {
    const mood = document.getElementById("moodInput").value;
    const res = document.getElementById("results");

    res.innerHTML = "Loading...";

    const response = await fetch(`${BASE_URL}/recommend-by-mood?mood=${mood}`);
    const data = await response.json();

    let html = "<h3>Mood Based Songs</h3><ul>";
    data.recommendations.forEach(r => {
        html += `<li>${r.song} — ${r.artist}</li>`;
    });
    html += "</ul>";

    res.innerHTML = html;
}
