$(document).ready(function() {
    var hre = document.getElementById("submit")
    var baseUrl = hre.getAttribute('href')
    
    console.log(baseUrl)
    console.log("script connected");

    var strLen = 0;
    var strOut = "";

    var gameField = $('div.gameContainer').find('div.box1');
    var gameBoard = gameField.find()
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

            var thisLetter = $(e);
            //console.log("blablabla: " + e);
            //console.log(gameField);
            console.log(thisLetter);
            var childIndex = 0;

            console.log(e.target);
            $(e.target).remove();
            $(thisLetter).remove();
            strLen--;
            changeOut();
            /*
            * var i = 0;
                while( (child = child.previousSibling) != null )
                  i++;
                //at the end i will contain the index.
            * */

        };
        gameField.append(letter);
        console.log("base:" + baseUrl,strOut)
        hre.setAttribute("href", baseUrl + strOut)
    });
    
    function changeOut(){
        //console.log(outputField);
        //console.log(strLen + ", " +strOut);
        outputField[0].innerHTML = strLen + ", \"" +strOut+"\"";
    }
});