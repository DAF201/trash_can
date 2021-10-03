async function start() {
    var input = document.getElementById('input').value
    document.getElementById('head').style.display = 'none'
    if (input != 'having a good time?') {
        document.getElementById('input').style.display = 'none'
        show();
        await sleep(12500);
        document.getElementById('hidden').style.display = 'block'
    } else {
        alert('welcome back home!')
        document.getElementById('tit').innerHTML = 'welcome back'
        document.getElementById('input').style.display = 'none'
        document.getElementById('red').style.display = 'block'
    }

}
function sleep(milliseconds) {
    return new Promise(resolve => setTimeout(resolve, milliseconds));
}
async function show() {
    var Welcome = 'Welcome to my summary page. The following parts will be a summary of things I have done over these three months, thank you.';
    var content = ''
    document.getElementById('welcome').style.display = 'block'
    for (let i in Welcome) {
        if (Welcome.charAt(i) == ',' || Welcome.charAt(i) == '.') {
            content = content + Welcome.charAt(i);
            document.getElementById('welcome').innerHTML = content
            await sleep(500);
        } else {
            content = content + Welcome.charAt(i);
            document.getElementById('welcome').innerHTML = content;
            await sleep(100);
        }
    }
    document.getElementById('wel2').style.display = 'block'
    await sleep(5000)
    document.getElementById('welcome').style.display = 'none'
    document.getElementById('wel2').style.display = 'none'
}
var lis = document;
lis.addEventListener('keyup',
    function (event) {
        if (event.keyCode === 13) {
            event.preventDefault();
            document.getElementById('head').click();
        }
    }
)
function show_paper() {
    document.getElementById('sp').style.display = 'none'
    document.getElementById('paper').style.display = 'block'
    document.getElementById('img2').style.display = 'block'
}