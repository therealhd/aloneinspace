function clickedProfile() {
    let elem = document.getElementById("profile_sub_list");
    let display = window.getComputedStyle(elem, null).getPropertyValue("display");

    if (display === 'none') {
        document.getElementById("profile_sub_list").style.display = "block"
    } else {
        document.getElementById("profile_sub_list").style.display = "none";
    }
}

function clickedLogin() {
    window.location.href = 'play'
}

function clickedPlay() {
    document.getElementById("play_button_div").style.display = "none"
    document.getElementById("game_frame").style.display = "block"
}