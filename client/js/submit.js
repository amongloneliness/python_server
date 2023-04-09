'use strict'

var port = 2000
var container__output = document.getElementsByClassName('container__output')
var container__input = document.getElementsByClassName('container__input')
let is_submit = false;     // статус выполнения функции submit

// асинхронная функция отправки POST запроса на сервер и получения обратного ответа
async function request_get(text) {
    let response = await fetch('http://localhost:' + port, {
            method: 'POST',
            body: text
        }
    );
    let resp_text = await response.text();

    return resp_text;
}

// прослушивание нажатия клавиши enter
container__input[0].addEventListener('keydown', e => {
    if (e.keyCode === 13) {
        return submit();
    }
})

// асинхронная функция задержки
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms))
}

// обработка события submit
function submit() {
    if (is_submit)
        return false;
    else
        is_submit = true;


    let text = 'v:' + document.getElementsByClassName('container__input')[0].value;
    let addr = 'http://localhost:' + port

    // посимвольное заполнение текстового блока
    request_get(text).then(data => {
        if (data.length == 0) {
            // завершение работы для следующего запуска
            is_submit = false;
            sumbit();
            return;
        }

        container__output[0].textContent = ''; 
        
        for (let i = 0; i < data.length; i++) {
            if (data[i] == '\n') {
                sleep(30 + i * 5).then(() => {container__output[0].innerHTML += '<br>';});
            } else if (data[i] == ' ') {
                sleep(30 + i * 5).then(() => {container__output[0].innerHTML += '&ensp;';});
            } else {
                sleep(30 + i * 5).then(() => {container__output[0].innerHTML += data[i];});
            }

            // завершение работы для следующего запуска
            if (i == data.length - 1) {
                sleep(30 + i * 5).then(() => is_submit = false);
            }
        }
    });

    return false;
}
   