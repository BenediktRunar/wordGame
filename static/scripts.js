$(document).ready(function() {
    var hre = document.getElementById("submit")
    var baseUrl = hre.getAttribute('href')
    
    console.log(baseUrl)
    console.log("script connected");

    var strLen = 0;
    var strOut = "";

    var gameField = $('div.gameContainer').find('div.box1');
    var gameBoard = gameField.find('div.gameBoard');
    var outputField = gameField.find('span.output');

    

    $('.letterBox').on('click', function(event) {
        var squareSelected = $(this);
        var letterInBox = squareSelected.find('h1')[0].innerText;
        console.log(letterInBox);
        strLen++;
        strOut += letterInBox;
        let letter = document.createElement("div");
        letter.className = "chosenLetter";
        letter.textContent = letterInBox;
        changeOut();

        letter.onclick = (e) => {
            var childIndex = -1;
            var thisChild = e.target;
            while((thisChild = thisChild.previousSibling) != null) {childIndex++;}

            console.log(childIndex);
            strOut = strOut.slice(0, childIndex) + strOut.slice(childIndex+1);
            $(e.target).remove();

            strLen--;
            changeOut();

        };
        gameBoard.append(letter);

        console.log("base:" + baseUrl,strOut)
        hre.setAttribute("href", baseUrl + strOut)
    });
    
    function changeOut(){
        outputField[0].innerHTML = strLen + ", \"" +strOut+"\"";
    }

    function getOutput(){
        return strOut;
    }
});