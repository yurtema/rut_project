 window.onload = function () {
        var box=document.getElementsByClassName('box');
        var btn=document.getElementById('button');
        for (let i=10;i<box.length;i++) {
            box[i].style.display = "none";
        }

        var countD = 10;
        btn.addEventListener("click", function() {
            var box=document.getElementsByClassName('box');
            countD += 10;
            if (countD <= box.length){
                for(let i=0;i<countD;i++){
                    box[i].style.display = "block";
                }
            }

        })
    }
