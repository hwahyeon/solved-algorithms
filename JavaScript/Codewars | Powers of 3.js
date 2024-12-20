function largestPower(n){
    const k = Math.floor(Math.log(n) / Math.log(3));
    return 3 ** k < n ? k : k - 1;
}
