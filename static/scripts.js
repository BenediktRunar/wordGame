$(document).ready(function() {
    var hre = document.getElementById("submit");
    var baseUrl = hre.getAttribute('href');
    var gameField = $('div.gameContainer').find('div.box1');
    var strLen = 0;
    var strOut = "";

    console.log(baseUrl)
    console.log("script connected");

    $('.letterBox').on('click', function(event) {

        var letterInBox = $(this).find('h1')[0].innerText;

        console.log(letterInBox);
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

        console.log("base:" + baseUrl,strOut);

        hre.setAttribute("href", baseUrl + strOut)
    });
    
    function changeOut(n){
        strLen += n;
        gameField.find('span.output')[0].innerHTML = strLen + ", \"" +strOut+"\"";
    }

    function getOutput(){
        return strOut;
    }
});

