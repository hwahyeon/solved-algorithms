function color(lambda) {
    if (lambda >= 620 && lambda <= 780) {
        return "Red";
    } else if (lambda >= 590 && lambda < 620) {
        return "Orange";
    } else if (lambda >= 570 && lambda < 590) {
        return "Yellow";
    } else if (lambda >= 495 && lambda < 570) {
        return "Green";
    } else if (lambda >= 450 && lambda < 495) {
        return "Blue";
    } else if (lambda >= 425 && lambda < 450) {
        return "Indigo";
    } else if (lambda >= 380 && lambda < 425) {
        return "Violet";
    }
}

const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString();
console.log(color(input));
