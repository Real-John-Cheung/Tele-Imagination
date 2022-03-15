function ver() {
    let tar = document.getElementById("live-streams");
    let h = document.getElementById("live-streams-board").clientHeight * 1.1 + "px";
    tar.style.height = h;
}

function unver() {
    document.getElementById("live-streams").removeAttribute('style');
}

let mql = window.matchMedia("(orientation: portrait)");
mql.addEventListener('change', () => {
    if (mql.matches) {
        ver();
    } else {
        unver();
    }
 });

window.onresize = () => {
    if (mql.matches) {
        ver();
    } else {
        unver();
    }
};
window.onload = () => {
    if (mql.matches) {
        ver();
    } else {
        unver();
    }
};



