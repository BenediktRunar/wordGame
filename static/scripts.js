var scoreList = [];
var wordList = [];


function printScore(input, word){
    word = new URL(word);
    var lastWord = word.searchParams.get("userWord");
    console.log('score was: ' + input + ", "+lastWord);
    wordList.push(lastWord);
    console.log(wordList);

    //var scoreField = $('div.gameContainer').find('div.box1').find('table.gameScore');

    var wordField = $('div.gameContainer').find('div.box1').find('div.scoreBoard')[0].lastElementChild;
    console.log(wordField);

    //var wordField = $('div.gameContainer').find('div.box1');
    //console.log(wordField);
    //wordField.append("<li>" + lastWord + "</li>");
    var newWord = document.createElement('li');
    newWord.innerHTML = lastWord;
    wordField.appendChild(newWord);
}

$(document).ready(function() {
    //Get existing url
    var hre = document.getElementById("submit");
    var baseUrl = hre.getAttribute('href');
    var gameField = $('div.gameContainer').find('div.box1');
    var strOut = "";
    var strLen = 0;


    $('.letterBox').on('click', function(event) {

        //A letter tile was clicked, getting its letter
        var letterInBox = $(this).find('h1')[0].innerText;
        //console.log(letterInBox);
        strOut += letterInBox;
        let letter = document.createElement("div");
        letter.className = "chosenLetter";
        letter.textContent = letterInBox;
        changeOut(1);

        var squareSelected = event.currentTarget;
        squareSelected.setAttribute("style", "visibility: hidden");

        letter.onclick = (e) => {
            var childIndex = -1;
            for(var child = e.target; child.previousSibling != null; child = child.previousSibling){
                childIndex++;
            }
            squareSelected.setAttribute("style", "visibility: block");
            strOut = strOut.slice(0, childIndex) + strOut.slice(childIndex+1);
            $(e.target).remove();
            changeOut(-1);
        };

        gameField.find('div.gameBoard').append(letter);

        // changing the href attrinbute
        hre.setAttribute("href", baseUrl + strOut)
        //console.log("here: " + hre.getAttribute('href'))
    });

    function changeOut(n){
        strLen += n;
        gameField.find('span.output')[0].innerHTML = strLen + ", \"" +strOut+"\"";
    }

    function getOutput(){
        return strOut;
    }
    function test(){
        console.log('function within ready scope');
    }

});


