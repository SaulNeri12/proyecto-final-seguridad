
const $cryptoModesField = document.querySelector('#crypto-modes-field');
const $encryptModeBtn = document.querySelector('#encrypt-mode');
const $decryptModeBtn = document.querySelector('#decrypt-mode');
const $plainTextKey = document.querySelector('#plain-text-key');
const $outputTextArea = document.querySelector('#output-text');
const $execBtn = document.querySelector('#execute-operation');
const $plainTextArea = document.querySelector('#plain-text');

function crypto(e) {
    var inputPlainText = $plainTextArea.value;
    var plainTextKey = $plainTextKey.value;
    var outputText;

    if ($encryptModeBtn.checked) {
        outputText = CryptoJS.AES.encrypt(inputPlainText, plainTextKey).toString();
        $outputTextArea.value = outputText;
    } else {
        outputText = CryptoJS.AES.decrypt(inputPlainText, plainTextKey).toString(CryptoJS.enc.Utf8);
        $outputTextArea.value = outputText;
    }
}

$cryptoModesField.addEventListener('change', () => {
    if ($encryptModeBtn.checked) {
        $execBtn.textContent = 'Encriptar';
    } else {
        $execBtn.textContent = 'Desencriptar';
    }
});

$execBtn.addEventListener('click', crypto);
